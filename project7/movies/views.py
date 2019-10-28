from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.
def index(request):

    return render(request, 'movies/index.html', {'movies' : Movie.objects.all()})

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    review = Review.objects.filter(movie_id=movie_pk)
    return render(request, 'movies/detail.html', {'movie': movie, 'form': form, 'reviews': review})

def review(request, movie_pk):
    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.user
            review.movie_id = Movie.objects.get(pk=movie_pk)
            review.save()
    return redirect('movies:detail', movie_pk)

def review_delete(request, movie_pk, review_pk):
    get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.user_id == request.user:
        if request.method == 'POST':
            review.delete()
    return redirect('movies:detail', movie_pk)
            
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST' and request.user.is_authenticated:
        if request.user in movie.like_movies_user.all():
            movie.like_movies_user.remove(request.user)
        else:
            movie.like_movies_user.add(request.user)
    return redirect('movies:detail', movie_pk)
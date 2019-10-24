from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
# Create your views here.

def index(request):
    return render(request, 'articles/index.html', {'articles': Article.objects.order_by('-id')})

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # 만든 사람
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    return render(request, 'articles/detail.html', {'article': article})

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'post':
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/update.html', {'form' : form})

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
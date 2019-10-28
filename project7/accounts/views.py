from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def userlist(request):
    users = get_user_model().objects.all()
    
    return render(request, 'accounts/userlist.html', {'userlist': users})

def profile(request, account_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=account_pk)
    context = {
        'user_profile' : user
    }
    return render(request, 'accounts/profile.html', context)



from .models import User as customUser
def follow(request, account_pk):
    User = get_user_model()
    movieuser = get_object_or_404(User, pk=account_pk)

    if movieuser != request.user:
        # movieuser를 팔로우한 적이 있다면
        if request.user in movieuser.followers.all():
            # 취소
            movieuser.followers.remove(request.user)
        # 아니면
        else:
            # 팔로우
            movieuser.followers.add(request.user)

    return redirect('accounts:profile', account_pk)
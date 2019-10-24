from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
# Create your views here.
def index(request):
   articles = Article.objects.all()
   return render(request, 'index.html', {'articles': articles})
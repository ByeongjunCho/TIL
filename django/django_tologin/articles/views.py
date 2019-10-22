from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.

def index(request):
    return render(request, 'articles/index.html', {'articles': Article.objects.order_by('-id')})
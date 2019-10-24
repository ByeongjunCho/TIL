from django import forms
from .models import Article, Comment
from django.contrib.auth import get_user_model
from django.conf import settings


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user', 'like',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user','article',)
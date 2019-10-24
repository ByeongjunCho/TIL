from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='models.CASCADE')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='articles', blank=True)

class Comment(models.Model):
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
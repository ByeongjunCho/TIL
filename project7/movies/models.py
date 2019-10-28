from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)  # 장르 구분

class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_movies_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie', blank=True)
    

class Review(models.Model):
    content = models.CharField(max_length=50)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
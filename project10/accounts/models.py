from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import settings
# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    
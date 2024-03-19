from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE, default=None)
    author = models.ForeignKey(User, models.CASCADE, default=None)
    #TODO: add many images support

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


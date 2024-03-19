from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE, default=None)
    #TODO: add many images support


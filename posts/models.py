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
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    #TODO: add many images support

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
    
    def like(self):
        self.like += 1
        return True
    
    def dislike(self):
        self.like -= 1
        return True


class PostImage(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    image = models.ImageField()
    image_replace_text = models.CharField(max_length=50)


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
    def like(self):
        self.like += 1
        return True
    
    def dislike(self):
        self.like -= 1
        return True


class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, models.CASCADE, default=None)
    image = models.ImageField()
    image_replace_text = models.CharField(max_length=50)
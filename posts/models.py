from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to='categories_pics/', default='default_category.jpg')

    def __str__(self):
        return f'NAME: {self.title}, SLUG: {self.slug}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE, default=None)
    author = models.ForeignKey(User, models.CASCADE, default=None)

    def __str__(self):
        return f'CATEGORY: {self.category.title}, AUTHOR: {self.author}, TITLE: {self.title}, SLUG: {self.slug}'

    def snippet(self):
        return self.body[:50] + '...'


class PostLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)

    def __str__(self):
        return f'USER: {self.user}, POST: {self.post.slug}'


class PostDisLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)

    def __str__(self):
        return f'USER: {self.user}, POST: {self.post.slug}'


class PostImage(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    image = models.ImageField(upload_to='post_pics/')

    def __str__(self):
        return f'POST: {self.post.slug}, IMG: {self.image}'


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'USER: {self.user}, POST: {self.post.slug}'


class CommentLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    comment = models.ForeignKey(Comment, models.CASCADE, default=None)


class CommentDisLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    comment = models.ForeignKey(Comment, models.CASCADE, default=None)


class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, models.CASCADE, default=None)
    image = models.ImageField()
    image_replace_text = models.CharField(max_length=50)
    user = models.ForeignKey(User, models.CASCADE, default=None)
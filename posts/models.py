from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to='categories_pics/', default='default_category.jpg')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.CASCADE, default=None)
    author = models.ForeignKey(User, models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class PostLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user}: liked {self.post}'


class PostDisLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user}: disliked {self.post}'


class PostImage(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    image = models.ImageField()

    def __str__(self):
        return f'Image of POST: {self.post.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    post = models.ForeignKey(Post, models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.user}: post {self.post}'


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
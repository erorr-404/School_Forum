from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'body',]


class CreateComment(forms.ModelForm):
    class Meta:
        text = models.Comment
        fields = ['text']
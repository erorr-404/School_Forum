from django import forms
from . import models


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CreatePost(forms.ModelForm):
    images = MultipleFileField(required=False)
    class Meta:
        model = models.Post
        fields = ['title', 'body']


class CreateComment(forms.ModelForm):
    class Meta:
        text = models.Comment
        fields = ['text']
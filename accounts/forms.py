from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False)
    biography = forms.CharField(required=False, widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'name', 'password1', 'password2', 'profile_picture', 'biography')

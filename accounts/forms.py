from re import U
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Set hashed password
        if commit:
            user.save()
            profile = Profile.objects.create(user=user)  # Create profile after user creation
        return user

class ProfileImageForm(forms.ModelForm):
    # def __init__(self, user=None):
    #     self.user= user
    
    class Meta:
        model = Profile
        fields = ('image', 'biography',)
    
    def save(self, user, commit=True):
        profile = super().save(commit=False)  # Save without saving to database yet
        # Access the user instance from the view (assuming it's passed in the context)
        existing_profile = Profile.objects.filter(user=profile.user).first()
        if existing_profile:
            existing_profile.image = profile.image
            existing_profile.biography = profile.biography
            existing_profile.save()
            return existing_profile
        else:
        # profile.user = user  # Replace 'user' with the actual context variable name
            if commit:
                profile.save()
            return profile

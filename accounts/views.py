from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register_view(request):
    return HttpResponse('Register')


def login_view(request):
    return HttpResponse('Login')


def edit_profile_view(request):
    return HttpResponse('Edit profile')


def profile_view(request):
    return HttpResponse('Your profile')
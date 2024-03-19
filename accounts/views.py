from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from .forms import RegistrationForm


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts:categories")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:categories")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})


def edit_profile_view(request):
    return HttpResponse('Edit profile')


def profile_view(request):
    return HttpResponse('Your profile')


def ajax_logout(request):
    if is_ajax(request):
        logout(request)
        response = {'first-text': 'Logged out'}
        return JsonResponse(response)
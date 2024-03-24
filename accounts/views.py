from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from .forms import *
from posts.models import *


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def register_view(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileImageForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            existing_profile = Profile.objects.filter(user=user).first()
            if existing_profile:
                existing_profile.image = profile_form.cleaned_data['image']
                existing_profile.save()
            else:
                profile_form.save(commit=False, user=user)
                profile_form.save(user)
            login(request, user)
            return redirect("posts:categories")
    else:
        user_form = RegistrationForm()
        profile_form = ProfileImageForm()
    return render(request, 'register.html', {'user_form':user_form, 'profile_form':profile_form})


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


def profile_view(request, username=''):
    if username == '':
        user = request.user
    else:
        user = User.objects.filter(username=username).first()
    
    posts_number = len(Post.objects.filter(author=user))
    if posts_number == 0:
        no_posts = True
    else:
        no_posts = False
    
    comments_number = len(Comment.objects.filter(user=user))
    if comments_number == 0:
        no_comments = True
    else:
        no_comments = False

    profile = Profile.objects.filter(user=user).first()
    user_stats = {
        'posts_number': posts_number,
        'last_posts': Post.objects.filter(author=user).order_by('date')[:5:-1],
        'no_posts': no_posts,
        'comments_number': comments_number,
        'last_comments': Comment.objects.filter(user=user).order_by('date')[:5:-1],
        'no_comments': no_comments,
        'likes_number': len(PostLike.objects.filter(user=user)) + len(CommentLike.objects.filter(user=user)),
        'dislikes_number': len(PostDisLike.objects.filter(user=user)) + len(CommentDisLike.objects.filter(user=user))}
    return render(request, 'profile.html', {'user':user, 'user_stats':user_stats, 'profile':profile})


def ajax_logout(request):
    if is_ajax(request):
        logout(request)
        response = {'first-text': 'Logged out'}
        return JsonResponse(response)
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Category, Post
from . import forms


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def categories_list_view(request):
    categories = Category.objects.all().order_by('date')
    return render(request, 'categories_list.html', {'categories': categories})


def post_list_view(request, category):
    posts = Post.objects.filter(Q(category__slug=category)).order_by('date')[::-1]
    return render(request, 'posts_list.html', {'posts':posts, 'category':category})


def post_view(request, category, post):
    post = Post.objects.get(slug=post)
    return render(request, 'post_detail.html', {'post':post})


@login_required(login_url='accounts:login')
def create_post(request, category):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.category = Category.objects.get(slug=category)
            instance.save()
            return redirect('posts:categories')
    else:
        form = forms.CreatePost()
    return render(request, 'create_post.html', {'form':form, 'category':category})


@login_required(login_url='accounts:login')
def like_post(request, category, post):
    if is_ajax(request):
        post.like()
        post.save()
        response = {'like-status': True}
    else:
        response = {'like-status': False}
    return JsonResponse(response)


@login_required(login_url='accounts:login')
def dislike_post(request, category, post):
    if is_ajax(request):
        post.dislike()
        post.save()
        response = {'dislike-status': True}
    else:
        response = {'dislike-status': False}
    return JsonResponse(response)
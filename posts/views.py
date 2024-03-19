from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post


# Create your views here.
def categories_list_view(request):
    categories = Category.objects.all().order_by('date')
    return render(request, 'categories_list.html', {'categories': categories})


def post_list_view(request, category):
    posts = Post.objects.filter(Q(category__slug=category)).order_by('date')[::-1]
    return render(request, 'posts_list.html', {'posts':posts})


def post_view(request, category, post):
    post = Post.objects.get(slug=post)
    return render(request, 'post_detail.html', {'post':post})
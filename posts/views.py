from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post

# Create your views here.
def categories_list_view(request):
    categories = Category.objects.all().order_by('date')[::-1]
    return render(request, 'categories_list.html', {'categories': categories})


def post_list_view(request, slug):
    return HttpResponse('Posts list')


def post_view(request):
    return HttpResponse('Post')
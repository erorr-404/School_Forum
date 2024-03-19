from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def categories_list_view(request):
    return HttpResponse('Categories list')


def post_list_view(request, slug):
    return HttpResponse('Posts list')


def post_view(request):
    return HttpResponse('Post')
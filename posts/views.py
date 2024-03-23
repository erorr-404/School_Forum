from cgitb import text
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from . import forms
from django.utils import timezone


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def categories_list_view(request):
    categories = Category.objects.all().order_by('date')
    return render(request, 'categories_list.html', {'categories': categories})


def post_list_view(request, category):
    posts = Post.objects.filter(Q(category__slug=category)).order_by('date')[::-1]
    user_profiles = []
    for post in posts:
        post_user_profile = Profile.objects.get(user=post.author)
        user_profiles.append(post_user_profile)
    zipped_list = zip(posts, user_profiles)
    return render(request, 'posts_list.html', {'posts':posts, 'category':category, 'profiles':user_profiles, 'zipped_list':zipped_list})


def post_view(request, category, post):
    post = Post.objects.get(slug=post)
    comments = Comment.objects.filter(post=post)[::-1]
    comments_users_profiles = []

    for comment in comments:
        comment_user_profile = Profile.objects.get(user=comment.user)
        comments_users_profiles.append(comment_user_profile)
    
    if len(comments) == 0:
        no_comments = True
    else:
        no_comments = False
    
    return render(request, 'post_detail.html', {'post': post,
                                                'author_profile': Profile.objects.get(user=post.author),
                                                'likes': len(PostLike.objects.filter(post=post)),
                                                'dislikes': len(PostDisLike.objects.filter(post=post)),
                                                'comments': comments,
                                                'zipped_comments': zip(comments, comments_users_profiles),
                                                'no_comments': no_comments,
                                                })


@login_required(login_url='accounts:login')
def create_post(request, category):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.category = Category.objects.get(slug=category)
            instance.save()
            return redirect(f'/{instance.category.slug}')
    else:
        form = forms.CreatePost()
    return render(request, 'create_post.html', {'form':form, 'category':category})


@login_required(login_url='accounts:login') # type: ignore
def like_post(request, category, post):
    if is_ajax(request):
        liked_post = Post.objects.get(slug=post)
        user_this_post_likes = len(PostLike.objects.filter(post=liked_post, user=request.user))
        user_this_post_dislikes = len(PostDisLike.objects.filter(post=liked_post, user=request.user))
        if user_this_post_likes == 0:
            like = PostLike(post=liked_post, user=request.user)
            like.save()
            like_status = True
            if user_this_post_dislikes > 0:
                PostDisLike.objects.filter(post=liked_post, user=request.user).delete()
                delete_dislike = True
            else:
                delete_dislike = False
        else:
            like_status = False
            delete_dislike = False

        response = {'likes': len(PostLike.objects.filter(post=liked_post)), 
                    'dislikes': len(PostDisLike.objects.filter(post=liked_post)), 
                    'like_status': like_status,
                    'delete_dislike': delete_dislike}
        return JsonResponse(response)


@login_required(login_url='accounts:login') # type: ignore
def dislike_post(request, category, post):
    if is_ajax(request):
        disliked_post = Post.objects.get(slug=post)
        user_this_post_likes = len(PostLike.objects.filter(post=disliked_post, user=request.user))
        user_this_post_dislikes = len(PostDisLike.objects.filter(post=disliked_post, user=request.user))
        if user_this_post_dislikes == 0:
            dislike = PostDisLike(post=disliked_post, user=request.user)
            dislike.save()
            dislike_status = True
            if user_this_post_likes > 0:
                PostLike.objects.filter(post=disliked_post, user=request.user).delete()
                delete_like = True
            else:
                delete_like = False
        else:
            dislike_status = False
            delete_like = False
    
        response = {'likes': len(PostLike.objects.filter(post=disliked_post)), 
                    'dislikes': len(PostDisLike.objects.filter(post=disliked_post)), 
                    'dislike_status': dislike_status,
                    'delete_like': delete_like}
        return JsonResponse(response)


@login_required(login_url='accounts:login') # type: ignore
def comment_post(request, category, post):
    if is_ajax(request):
        comment_text = request.POST.get('text')
        if comment_text != '' and ' ':
            comment_user = request.user
            comment_profile_image = Profile.objects.get(user=request.user).image.url
            comment_date = timezone.now()
            comment_post = Post.objects.get(slug=post)

            comment = Comment(user=comment_user, post=comment_post, text=comment_text)
            comment.save()

            return JsonResponse({'text': comment_text, 
                                 'user_name': comment_user.username, 
                                 'profile_image_url': comment_profile_image, 
                                 'comment_date': comment_date})

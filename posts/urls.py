from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.categories_list_view, name='categories'),
    path('<slug:category>/create', views.create_post, name='create'),
    path('<slug:category>', views.post_list_view, name='posts_list'),
    path('<slug:category>/<slug:post>', views.post_view, name='show'),
    path('<slug:category>/<slug:post>/like/', views.like_post, name='like_post'),
    path('<slug:category>/<slug:post>/dislike/', views.dislike_post, name='dislike_post'),
]
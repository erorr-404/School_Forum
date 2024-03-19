from django.urls import path
from . import views


urlpatterns = [
    path('', views.categories_list_view, name='categories'),
    path('<slug:category>', views.post_list_view, name='posts_list'),
    path('<slug:category>/<slug:post>', views.post_view)
]
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('ajax-logout/', views.ajax_logout, name='ajax_logout'),
]
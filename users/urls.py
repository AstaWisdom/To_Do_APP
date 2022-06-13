"""Defines ulrs patterns for users"""
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = (
    # Include default auth path
    path('', include('django.contrib.auth.urls')),
    # User registration page
    path('register/', views.register, name='register'),
    # User Profile Page
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    # set profile picutre
    path('profile_picture/<int:user_id>', views.profile_picture, name='profile_picture'),
)

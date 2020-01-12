"""DevelopersToolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from blog import views as blog

urlpatterns = [
    path('', blog.home, name='blog_home'),
    path('gallery/', blog.gallery, name='blog_gallery'),
    path('gallery/<str:title>/', blog.gallery_item, name='blog_gallery_item'),
    path('tutorials/', blog.tutorial, name='blog_tutorial'),
    path('tutorials/<str:title>/', blog.tutorial_item, name='blog_tutorial_item'),
    path('tutorials/<str:title>/<int:index>/', blog.tutorial_item_index, name='blog_tutorial_item_index'),
    path('news/', blog.news, name='blog_news'),
]

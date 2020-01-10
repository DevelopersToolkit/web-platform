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
from app import forms, views as app

urlpatterns = [
    path('', app.home, name='home'),
    path('contact/', app.contact, name='contact'),
    path('about/', app.about, name='about'),
    path('login/', LoginView.as_view(
        template_name='app/login.html',
        authentication_form=forms.BootstrapAuthenticationForm,
        extra_context={'title': 'Log in', 'year': datetime.now().year}
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
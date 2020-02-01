"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from .models import Profile
# Create your views here.


def home(request):
    """Renders the home page"""
    assert isinstance(request, HttpRequest)
    template = 'app/home.html'
    context = {'title': 'Home', 'year': datetime.now().year}
    return render(request, template, context)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    template = 'app/contact.html'
    context = {'title': 'Contact', 'year': datetime.now().year}
    query_users_tier1 = Profile.objects.filter(role=1)
    query_users_tier2 = Profile.objects.filter(role=2)
    query_users_tier3 = Profile.objects.filter(role=3)
    context['tier1_users'] = query_users_tier1
    context['tier2_users'] = query_users_tier2
    context['tier3_users'] = query_users_tier3
    return render(request, template, context)


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {'title': 'About', 'message': 'Your application description page.', 'year': datetime.now().year}
    )


def profile(request):
    """Display user profile info and allow profile update"""
    assert isinstance(request, HttpRequest)
    template = 'app/profile.html'
    context = {}
    return render(request, template, context)

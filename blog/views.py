"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
# Create your views here.


def home(request):
    """Renders the home page"""
    assert isinstance(request, HttpRequest)
    template = 'blog/home.html'
    context = {'title': 'Home', 'year': datetime.now().year}
    return render(request, template, context)


def gallery(request):
    """Renders the gallery"""
    assert isinstance(request, HttpRequest)
    template = 'blog/gallery.html'
    context = {'title': 'Gallery', 'year': datetime.now().year}
    return render(request, template, context)


def gallery_item(request, title):
    # TODO query gallery table to collect the specified gallery for display
    """Renders a gallery post"""
    assert isinstance(request, HttpRequest)
    template = ''
    context = {}
    return render(request, template, context)


def tutorial(request):
    # TODO perform query to show/sort all tutorials and pagination type things
    """Renders tutorials list"""
    assert isinstance(request, HttpRequest)
    template = ''
    context = {}
    return render(request, template, context)


def tutorial_item(request, title):
    # TODO perform query to grab a specific tutorial series
    """Renders a tutorial series matching the provided title"""
    assert isinstance(request, HttpRequest)
    template = ''
    context = {}
    return render(request, template, context)


def tutorial_item_index(request, title, index):
    # TODO page switching between tutorial sections (like a playlist, this view may be unnecessary)
    """Renders a tutorial item in a series matching a series title and location index"""
    assert isinstance(request, HttpRequest)
    template = ''
    context = {}
    return render(request, template, context)


def news(request):
    # TODO news display all news items, decide on query type/structure
    """Renders news page"""
    assert isinstance(request, HttpRequest)
    template = ''
    context = {}
    return render(request, template, context)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {'title': 'Contact', 'message': 'Your contact page.', 'year': datetime.now().year}
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {'title': 'About', 'message': 'Your application description page.', 'year': datetime.now().year}
    )

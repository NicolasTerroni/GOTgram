"""Posts views."""

# Utilities
from datetime import datetime

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

posts = [
    {
        'title': 'Training day',
        'user': {
            'name': 'jon.snow',
            'picture': 'https://i.ibb.co/WB58sgN/jon-profile.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/wC7fV4Q/jon-training.jpg',
    },
    {
        'title': 'Old friend',
        'user': {
            'name': 'arya',
            'picture': 'https://i.ibb.co/nrhYxwy/arya-profile.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/b7pJWCX/arya-hound.jpg',
    },
    {
        'title': '#TBT',
        'user': {
            'name': 'jlannister',
            'picture': 'https://i.ibb.co/D7sQT2g/jamie-profile.png'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/3dhYWgS/jaime-throne.jpg',
    }
]

@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, "posts/feed.html", {"posts": posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = PostForm()
    
    return render(
        request=request,
        template_name="posts/new.html",
        context={
            "form" : form,
            "user" : request.user,
            "profile": request.user.profile
        }
    )
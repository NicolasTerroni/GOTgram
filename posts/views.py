"""Posts views."""

# Utilities
from datetime import datetime

# Django
from django.shortcuts import render

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

def list_posts(request):
    """List existing posts."""
    return render(request, "posts/feed.html", {"posts": posts})


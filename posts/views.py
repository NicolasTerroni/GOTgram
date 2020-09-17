"""Posts views."""

# Utilities
from datetime import datetime

# Django
from django.http import HttpResponse



def list_posts(request):
    """List existing posts."""
    posts = [1, 2, 3]
    return HttpResponse(str(posts))
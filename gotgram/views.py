"""gotgram views"""

# Utilities
from datetime import datetime

# Django
from django.http import HttpResponse


def hello(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Current server time: {str(now)}")

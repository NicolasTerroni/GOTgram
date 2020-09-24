"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model.
    Proxy model that extends existing user model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    biography = models.TextField(max_length=200, blank=True)
    
    profile_picture = models.ImageField(
        upload_to='users/pictures', 
        blank=True, 
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return users string representation."""
        return self.user.username
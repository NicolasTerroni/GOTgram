"""Posts models."""

# Django
from django.db import models

class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=50)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns user info."""
        return (f"""
        -------------------------------------
        - User ID: {self.id} 
        - Name: {self.first_name} 
        - Email: {self.email}
        """)
    
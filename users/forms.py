"""User forms."""

# Django
from django import forms


class ProfileForm(forms.Form):
    """Profile form."""

    profile_picture = forms.ImageField()
    biography = forms.CharField(max_length=500, required=False)

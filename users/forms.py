"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(
        label=False,
        min_length=4,
        max_length=50, 
        widget = forms.TextInput(attrs={'placeholder':'Username','class': 'form-control','required': True}))

    password = forms.CharField(
        label=False,
        min_length=8, 
        max_length=70, 
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control','required': True}))
    password_confirmation = forms.CharField(
        label=False,
        min_length=8, 
        max_length=70, 
        widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation','class': 'form-control','required': True}))

    first_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'First name','class': 'form-control','required': True}))
    last_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'Last name','class': 'form-control','required': True}))

    email = forms.CharField(
        label=False,
        min_length=6, 
        max_length=70, 
        widget=forms.TextInput(attrs={'placeholder':'Email','class': 'form-control','required': True}))


    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError("Username is already in use.")
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise forms.ValidationError("Password confirmation does not match.")
        return data
    
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop("password_confirmation")

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()



class ProfileForm(forms.Form):
    """Profile form."""

    profile_picture = forms.ImageField()
    biography = forms.CharField(max_length=500, required=False)

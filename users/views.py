"""Users views."""

# Python
import pdb

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import DetailView, FormView
from django.urls import reverse_lazy

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Forms
from users.forms import ProfileForm, SignupForm

class UserDetailView(LoginRequiredMixin,DetailView):
    """Users detail view."""

    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by("-created")
        return context


class SignUpView(FormView):
    """Sign up form view."""
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.profile_picture = data['profile_picture']
            profile.biography = data['biography']
            profile.save()

            messages.success(request, 'Your profile has been updated!')

            url = reverse('users:detail', kwargs={"username": request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')
    

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect("users:login")
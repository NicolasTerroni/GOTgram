"""gotgram URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Local
from gotgram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path("hello/",local_views.hello ,name="hello"),

    path('admin/', admin.site.urls, name="admin"),

    path("posts/",posts_views.list_posts, name="feed"),

    path("users/login/", users_views.login_view, name="login"),
    path("users/logout/", users_views.logout_view, name="logout"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
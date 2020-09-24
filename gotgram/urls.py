"""gotgram URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Local
from gotgram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path("hello/",local_views.hello),

    path('admin/', admin.site.urls),

    path("posts/",posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
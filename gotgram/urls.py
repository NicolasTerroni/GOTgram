"""gotgram URL Configuration"""

from django.contrib import admin
from django.urls import path
from gotgram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path("hello/",local_views.hello),

    path("posts/",posts_views.list_posts),
]

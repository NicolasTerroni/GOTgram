"""Posts admin configuration."""

# Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'profile',
        'title',
        'photo',
        'created',
    )

    list_display_links = (
        'pk',
        'user',
    )

    search_fields = (
        'pk',
        'user__username',
    )

    list_filter = (
        'created',
        'modified'
    )

    readonly_fields = ('created','modified')
    

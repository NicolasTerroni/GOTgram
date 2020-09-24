"""Users admin configuration."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = (
        'pk',
        'user',
        'profile_picture',
        'biography',
        'created',
        'modified',
    )

    list_editable = (
        'biography',
    )

    list_display_links = (
        'pk',
        'user',
    )

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'pk',
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',    
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user','profile_picture'),)
        }),
        ('Extra info', {
            'fields': ('biography',)
        }),
        ('Metadata', {
            'fields': (('created','modified'),)
        })
    )
    readonly_fields = ('created','modified','user')


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
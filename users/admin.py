# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# models
from users.models import Profile

@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    """User Profile"""
    list_display = ('pk', 'user', 'phone_number', 'country')
    list_display_links = ('user',)
    search_fields= (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter= (
        'user__is_active',
        'user__is_staff'
    )
    fieldsets = (
        (
            'Info',
            {
                'fields': (
                    ('user'),
                    ('phone_number', 'photo'),
                )
            }
        ),
        (
            'Address Info', 
            {
                'fields': (
                    ('country', 'state', 'city', 'address', 'postal_code')
                )
            }
        ),
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles Users'

class ProfileAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

#Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
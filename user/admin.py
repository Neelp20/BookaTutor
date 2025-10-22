from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    # Disable the "Add" button for existing users
    def has_add_permission(self, request):
        return False  # Only allow editing

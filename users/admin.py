from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Register User model to admin panel"""
    list_display = ['id', 'email', 'first_name', 'last_name']
    list_display_links = list_display
    search_fields = ['email']
    fields = ['email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']

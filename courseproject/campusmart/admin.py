from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'name', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'name')

admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import GrinchUser
from users.forms import GrinchUserCreationForm, GrinchUserChangeForm


class GrinchUserAdmin(UserAdmin):
    add_form = GrinchUserCreationForm
    form = GrinchUserChangeForm
    model = GrinchUser
    list_display = ("username", "first_name", "last_name", "email", "route")
    list_filter = ("username", "is_staff", "is_active")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Route Assignment', {'fields': ('route',)})
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(GrinchUser, GrinchUserAdmin)

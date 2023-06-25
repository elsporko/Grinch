from django.contrib import admin
from users.models import GrinchUser

@admin.register(GrinchUser)
class GrinchUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "route", "email")

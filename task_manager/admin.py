from django.contrib import admin
from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'user_name', "time_create")
    list_display_links = ("first_name",)
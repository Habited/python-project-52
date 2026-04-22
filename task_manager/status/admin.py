from django.contrib import admin
from .models import Statuses

@admin.register(Statuses)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']
from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'status', 'author', 'time_create']
    list_filter = ['status', 'time_create']
    search_fields = ['task_name', 'description']

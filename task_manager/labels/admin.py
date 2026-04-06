from django.contrib import admin
from .models import Label

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['label_name', 'time_create']
    list_filter = ['time_create']
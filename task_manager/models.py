from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(blank=True)
    user_name = models.TextField(blank=True)
    password = models.CharField(max_length=255, blank=True)
    password_validation = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)



from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.TextField(blank=True, verbose_name="Фамилия")
    user_name = models.TextField(blank=True, verbose_name="Имя пользователя")
    password = models.CharField(max_length=255, blank=True, verbose_name="Пароль")
    password_validation = models.CharField(max_length=255, blank=True, verbose_name="Подтвердить пароль")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class Statuses(models.Model):
    status_name = models.CharField(max_length=255, verbose_name="Имя")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

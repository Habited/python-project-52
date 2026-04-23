from django.db import models
from task_manager.status.models import Statuses
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model

User = get_user_model()


class Tasks(models.Model):
    task_name = models.CharField(
        max_length=255, 
        verbose_name="Имя",
        unique=True)
    description = models.TextField(
        verbose_name="Описание",
        )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.CASCADE,
        verbose_name="Статус",
        related_name="status_tasks",
        null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Автор",
        related_name="author_tasks",
        null=False,)
    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Исполнитель",
        related_name="executor_tasks",
        blank=True,
        null=True)
    labels = models.ManyToManyField(
        Label,
        related_name="tasks",
        blank=True)
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ['-time_create']
    
    def __str__(self):
        return self.task_name


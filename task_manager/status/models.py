from django.db import models

class Statuses(models.Model):
    status_name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
    
    def __str__(self):
        return self.status_name

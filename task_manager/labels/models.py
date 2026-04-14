from django.db import models


class Label(models.Model):
    label_name = models.CharField(max_length=255, verbose_name="Имя", unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Метки"
    
    def __str__(self):
        return self.label_name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    name = models.CharField("Дело", max_length=100)
    description = models.CharField("Описание", max_length=1000, blank=True)
    is_done = models.BooleanField("Состояние")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Пользователь - {self.user}; Задача - {self.name[:30]}"

    class Meta:
        ordering = ["is_done", "created_at",]



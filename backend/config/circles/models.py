from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Circle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    name = models.CharField("Название", max_length=200)
    time_period = models.PositiveSmallIntegerField("Длительность")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Задача {self.name} - длитеьность - {self.time_period}"
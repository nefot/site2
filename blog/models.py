from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название статьи")
    subtitle = models.CharField(max_length=2550000, verbose_name="Текст статьи")
    time = models.DateTimeField(auto_now=False, default=timezone.now, verbose_name="дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блоги"
        verbose_name_plural = "Блоги"


def __str__(self):
    return self.title

from django.db import models
from django.utils import timezone



class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя качка")
    subtitle = models.CharField(max_length=255, verbose_name="Характеристика качка")
    functions = models.CharField(max_length=100, verbose_name="Функции качка", default="Бездарь")
    image = models.ImageField(upload_to='portfolio/images/', verbose_name="Фото качка")
    time = models.DateTimeField(auto_now=False, default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Качка"
        verbose_name_plural = "Список качков"

class Memes(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название мема")
    image = models.ImageField(upload_to='portfolio/images/', verbose_name="Фото качка")
    time = models.DateTimeField(auto_now=False, default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мемы"
        verbose_name_plural = "Список Мемов"

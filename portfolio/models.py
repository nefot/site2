from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files import File
from PIL import Image

def make_thumbnail(image, size=(100, 100)):
    """Создает миниатюры заданного размера"""
    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=60)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


class Almanac(models.Model):
    task = models.CharField(max_length=100, verbose_name = 'Название предмета')
    # name = models.CharField(max_length=100, verbose_name = 'Имя преподавателя')
    # time = models.DateTimeField('время пары')

    monday   = models.BooleanField(default = 0, verbose_name = 'monday'  )
    tuesday  = models.BooleanField(default = 0, verbose_name = 'tuesday' )
    wensday  = models.BooleanField(default = 0, verbose_name = 'wensday' )
    thursdy  = models.BooleanField(default = 0, verbose_name = 'thursdy' )
    friday   = models.BooleanField(default = 0, verbose_name = 'friday'  )
    saturday = models.BooleanField(default = 0, verbose_name = 'saturday')
    sunday   = models.BooleanField(default = 0, verbose_name = 'sunday'  )

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание недели"


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя качка")
    subtitle = models.CharField(max_length=500, verbose_name="Характеристика качка")
    functions = models.CharField(max_length=500, verbose_name="Функции качка", default="Бездарь")
    image = models.ImageField(upload_to='portfolio/images/', verbose_name="Фото качка")
    print(image)
    print(type(image))
    time = models.DateTimeField(auto_now=False, default=timezone.now)
    is_published = models.BooleanField(default=True)
    money = models.IntegerField(default=0, verbose_name="Монеты")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image = make_thumbnail(self.image, size=(500, 500))
        super().save(*args, **kwargs)

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

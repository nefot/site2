from encodings import search_function

from django.contrib import admin

from .models import *



class Person(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'time', 'is_published']
    list_display_links = ['title','time']
    search_fields = ('title','time')
    list_editable = ['is_published']

# title = models.CharField(max_length=100, verbose_name="Имя качка")
#     subtitle = models.CharField(max_length=255, verbose_name="Характеристика качка")
#     image = models.ImageField(upload_to='portfolio/images/', verbose_name="Фото качка")
#     time

admin.site.register(Project, Person)

admin.site.register(Memes)

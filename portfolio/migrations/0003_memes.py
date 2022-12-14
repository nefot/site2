# Generated by Django 4.1.2 on 2022-12-10 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_remove_project_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мема')),
                ('image', models.ImageField(upload_to='portfolio/images/', verbose_name='Фото качка')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Мемы',
                'verbose_name_plural': 'Список Мемов',
            },
        ),
    ]

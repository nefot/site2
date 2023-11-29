# Generated by Django 4.2.7 on 2023-11-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_memes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=0, verbose_name='monday')),
                ('tuesday', models.BooleanField(default=0, verbose_name='tuesday')),
                ('wensday', models.BooleanField(default=0, verbose_name='wensday')),
                ('thursdy', models.BooleanField(default=0, verbose_name='thursdy')),
                ('friday', models.BooleanField(default=0, verbose_name='friday')),
                ('saturday', models.BooleanField(default=0, verbose_name='saturday')),
                ('sunday', models.BooleanField(default=0, verbose_name='sunday')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание недели',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='money',
            field=models.IntegerField(default=0, verbose_name='Монеты'),
        ),
        migrations.AlterField(
            model_name='project',
            name='functions',
            field=models.CharField(default='Бездарь', max_length=500, verbose_name='Функции качка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.CharField(max_length=500, verbose_name='Характеристика качка'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-20 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_calendar_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calendar',
            new_name='Almanac',
        ),
    ]
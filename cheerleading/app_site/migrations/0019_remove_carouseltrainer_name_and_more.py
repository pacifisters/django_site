# Generated by Django 4.0.4 on 2022-05-23 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0018_remove_carouselhead_name_carouselhead_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouseltrainer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='titleshortcuticon',
            name='name',
        ),
    ]

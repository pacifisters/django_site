# Generated by Django 4.0.4 on 2022-07-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0034_clubfoto_foto_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubfoto',
            name='foto_1',
        ),
    ]

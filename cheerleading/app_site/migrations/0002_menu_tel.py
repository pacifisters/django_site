# Generated by Django 4.0.4 on 2022-05-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='tel',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0012_menu_title_1_menu_title_2_menu_title_3_menu_title_4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='btn_name_1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='menu',
            name='btn_name_4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='menu',
            name='btn_name_menu',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='menu',
            name='text_1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='text_3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='text_4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

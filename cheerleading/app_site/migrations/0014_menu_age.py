# Generated by Django 4.0.4 on 2022-05-23 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0013_menu_btn_name_1_menu_btn_name_4_menu_btn_name_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='age',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_site.agecard'),
            preserve_default=False,
        ),
    ]

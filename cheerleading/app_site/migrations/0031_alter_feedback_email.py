# Generated by Django 4.0.4 on 2022-06-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0030_alter_menu_social_data_1_alter_menu_social_data_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
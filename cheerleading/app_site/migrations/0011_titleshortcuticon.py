# Generated by Django 4.0.4 on 2022-05-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0010_agecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleShortcutIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='редактировать_title_&_shortcut_icon', max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('img', models.FileField(upload_to='files/')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0021_contacts_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.menu')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0023_delete_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='footer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

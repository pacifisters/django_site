# Generated by Django 4.0.4 on 2022-07-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0033_remove_menu_a_faq_remove_menu_q_faq_faq_clubfoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubfoto',
            name='foto_1',
            field=models.FileField(default=1, upload_to='files/', verbose_name='foto1'),
            preserve_default=False,
        ),
    ]

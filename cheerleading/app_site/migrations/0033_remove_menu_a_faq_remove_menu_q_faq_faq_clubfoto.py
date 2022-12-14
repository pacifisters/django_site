# Generated by Django 4.0.4 on 2022-07-18 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0032_rename_text_3_menu_a_faq_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='a_faq',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='q_faq',
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_faq', models.TextField(verbose_name='вопрос')),
                ('a_faq', models.TextField(verbose_name='ответ')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.menu')),
            ],
        ),
        migrations.CreateModel(
            name='ClubFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='files/', verbose_name='foto')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.menu')),
            ],
        ),
    ]

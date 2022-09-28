# Generated by Django 4.0.4 on 2022-05-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30)),
                ('item_1', models.CharField(blank=True, max_length=30)),
                ('item_2', models.CharField(blank=True, max_length=30)),
                ('item_3', models.CharField(blank=True, max_length=30)),
                ('item_4', models.CharField(blank=True, max_length=30)),
                ('item_5', models.CharField(blank=True, max_length=30)),
                ('social_img_1', models.FileField(upload_to='files/')),
                ('social_data_1', models.CharField(blank=True, max_length=30)),
                ('social_img_2', models.FileField(upload_to='files/')),
                ('social_data_2', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
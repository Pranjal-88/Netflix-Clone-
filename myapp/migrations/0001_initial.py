# Generated by Django 5.0.6 on 2024-06-08 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100000)),
                ('duration', models.PositiveIntegerField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('thriller', 'Thriller')], max_length=30)),
                ('img_card', models.ImageField(upload_to='movie_cards')),
                ('release_data', models.DateField(default=datetime.datetime.now)),
                ('added_to_list', models.BooleanField(default=False)),
            ],
        ),
    ]

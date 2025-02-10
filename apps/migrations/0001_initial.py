# Generated by Django 5.1.5 on 2025-01-19 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=500)),
                ('num', models.TextField()),
                ('email', models.EmailField(max_length=400)),
                ('message', models.TextField()),
            ],
        ),
    ]

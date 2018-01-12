# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=50, unique=True)),
                ('is_verified', models.BooleanField()),
                ('location', models.CharField(max_length=50)),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findfriends.TwitterUser')),
            ],
        ),
    ]

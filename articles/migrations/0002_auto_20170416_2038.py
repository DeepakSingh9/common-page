# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 16, 15, 8, 6, 317000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
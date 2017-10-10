# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 17:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 6, 17, 30, 24, 550417, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
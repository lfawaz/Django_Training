# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171006_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 6, 18, 21, 17, 624504, tzinfo=utc)),
        ),
    ]

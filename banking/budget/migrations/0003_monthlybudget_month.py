# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-25 16:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20160825_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlybudget',
            name='month',
            field=models.DateField(default=datetime.datetime(2016, 8, 25, 16, 32, 52, 596200, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

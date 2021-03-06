# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cash', models.DecimalField(decimal_places=2, max_digits=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]

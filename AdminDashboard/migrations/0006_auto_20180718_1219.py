# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-18 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0005_auto_20180717_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
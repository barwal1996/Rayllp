# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-16 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeDashboard', '0002_auto_20180715_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportwork',
            name='work_content',
        ),
        migrations.RemoveField(
            model_name='reportwork',
            name='work_date',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-17 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeDashboard', '0004_reportwork_emp_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('emp_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EmployeeDashboard.EmployeeProfile')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
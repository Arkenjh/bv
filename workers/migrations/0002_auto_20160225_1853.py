# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='workplace',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workers.Workplaces'),
        ),
    ]

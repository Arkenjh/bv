# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20160315_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Stores', unique_for_date='date', verbose_name='magasin'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstores',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nom'),
        ),
    ]
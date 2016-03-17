# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(verbose_name='commentaire'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ajouté le'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.Comments', verbose_name='commentaire'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='qty_inkjet_1',
            field=models.IntegerField(default=0, verbose_name='Qte JE 1'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='qty_inkjet_2',
            field=models.IntegerField(default=0, verbose_name='Qte JE 2'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='qty_laser_1',
            field=models.IntegerField(default=0, verbose_name='Qte LA 1'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='qty_laser_2',
            field=models.IntegerField(default=0, verbose_name='Qte LA 2'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.Stores', unique_for_date='date', verbose_name='magasin'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='modifié le'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='workers',
            field=models.ManyToManyField(to='workers.Workers', verbose_name='employé(s)'),
        ),
    ]
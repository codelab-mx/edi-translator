# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_mining', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SHP_7',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_mining', '0004_auto_20160802_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_segments_master',
            name='SDP_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='SDP_2',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

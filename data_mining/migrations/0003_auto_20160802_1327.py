# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_mining', '0002_auto_20160802_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_segments_fst',
            name='prim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_830LIN'),
        ),
    ]

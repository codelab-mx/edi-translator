# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-08 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo_GS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GS_1', models.CharField(blank=True, max_length=50)),
                ('GS_2', models.CharField(blank=True, max_length=50)),
                ('GS_3', models.CharField(blank=True, max_length=50)),
                ('GS_4', models.CharField(blank=True, max_length=50)),
                ('GS_5', models.CharField(blank=True, max_length=50)),
                ('GS_6', models.CharField(blank=True, max_length=50)),
                ('GS_7', models.CharField(blank=True, max_length=50)),
                ('GS_8', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]

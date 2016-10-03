# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Name', models.CharField(max_length=100)),
                ('C_Edi_Address', models.CharField(max_length=50)),
                ('C_Country', models.CharField(blank=True, max_length=100)),
                ('C_City', models.CharField(blank=True, max_length=100)),
                ('C_ZIP', models.CharField(blank=True, max_length=100)),
                ('C_E_mail', models.CharField(blank=True, max_length=100)),
                ('C_Phone', models.CharField(blank=True, max_length=100)),
                ('C_Address', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Name', models.CharField(max_length=100)),
                ('P_Edi_Address', models.CharField(max_length=50)),
                ('P_Country', models.CharField(blank=True, max_length=100)),
                ('P_City', models.CharField(blank=True, max_length=100)),
                ('P_ZIP', models.CharField(blank=True, max_length=100)),
                ('P_E_mail', models.CharField(blank=True, max_length=100)),
                ('P_Phone', models.CharField(blank=True, max_length=100)),
                ('P_Address', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

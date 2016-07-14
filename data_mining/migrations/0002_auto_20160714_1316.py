# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-14 18:16
from __future__ import unicode_literals

import data_mining.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_mining', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edi_address',
            name='edi_file',
            field=models.FileField(upload_to='edi/', validators=[data_mining.validators.file_size]),
        ),
    ]

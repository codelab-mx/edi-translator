# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 22:34
from __future__ import unicode_literals

import data_mining.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_segments_830LIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LIN_1', models.CharField(blank=True, max_length=50)),
                ('LIN_2', models.CharField(blank=True, max_length=50)),
                ('LIN_3', models.CharField(blank=True, max_length=50)),
                ('LIN_4', models.CharField(blank=True, max_length=50)),
                ('LIN_5', models.CharField(blank=True, max_length=50)),
                ('LIN_6', models.CharField(blank=True, max_length=50)),
                ('LIN_7', models.CharField(blank=True, max_length=50)),
                ('LIN_8', models.CharField(blank=True, max_length=50)),
                ('LIN_9', models.CharField(blank=True, max_length=50)),
                ('LIN_10', models.CharField(blank=True, max_length=50)),
                ('LIN_11', models.CharField(blank=True, max_length=50)),
                ('LIN_12', models.CharField(blank=True, max_length=50)),
                ('LIN_13', models.CharField(blank=True, max_length=50)),
                ('LIN_14', models.CharField(blank=True, max_length=50)),
                ('LIN_15', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_862LIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LIN_1', models.CharField(blank=True, max_length=50)),
                ('LIN_2', models.CharField(blank=True, max_length=50)),
                ('LIN_3', models.CharField(blank=True, max_length=50)),
                ('LIN_4', models.CharField(blank=True, max_length=50)),
                ('LIN_5', models.CharField(blank=True, max_length=50)),
                ('LIN_6', models.CharField(blank=True, max_length=50)),
                ('LIN_7', models.CharField(blank=True, max_length=50)),
                ('LIN_8', models.CharField(blank=True, max_length=50)),
                ('LIN_9', models.CharField(blank=True, max_length=50)),
                ('LIN_10', models.CharField(blank=True, max_length=50)),
                ('LIN_11', models.CharField(blank=True, max_length=50)),
                ('LIN_12', models.CharField(blank=True, max_length=50)),
                ('LIN_13', models.CharField(blank=True, max_length=50)),
                ('LIN_14', models.CharField(blank=True, max_length=50)),
                ('LIN_15', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_ATH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ATH_0', models.CharField(blank=True, max_length=50)),
                ('ATH_1', models.CharField(blank=True, max_length=50)),
                ('ATH_2', models.CharField(blank=True, max_length=50)),
                ('ATH_3', models.CharField(blank=True, max_length=50)),
                ('ATH_4', models.CharField(blank=True, max_length=50)),
                ('ATH_5', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_BFR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BFR_1', models.CharField(blank=True, max_length=50)),
                ('BFR_2', models.CharField(blank=True, max_length=50)),
                ('BFR_3', models.CharField(blank=True, max_length=50)),
                ('BFR_4', models.CharField(blank=True, max_length=50)),
                ('BFR_5', models.CharField(blank=True, max_length=50)),
                ('BFR_6', models.CharField(blank=True, max_length=50)),
                ('BFR_7', models.CharField(blank=True, max_length=50)),
                ('BFR_8', models.CharField(blank=True, max_length=50)),
                ('BFR_11', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_BSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BSS_1', models.CharField(blank=True, max_length=50)),
                ('BSS_2', models.CharField(blank=True, max_length=50)),
                ('BSS_3', models.CharField(blank=True, max_length=50)),
                ('BSS_4', models.CharField(blank=True, max_length=50)),
                ('BSS_5', models.CharField(blank=True, max_length=50)),
                ('BSS_6', models.CharField(blank=True, max_length=50)),
                ('BSS_7', models.CharField(blank=True, max_length=50)),
                ('BSS_8', models.CharField(blank=True, max_length=50)),
                ('BSS_11', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_FST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FST_0', models.CharField(blank=True, max_length=50)),
                ('FST_1', models.CharField(blank=True, max_length=50)),
                ('FST_2', models.CharField(blank=True, max_length=50)),
                ('FST_3', models.CharField(blank=True, max_length=50)),
                ('FST_4', models.CharField(blank=True, max_length=50)),
                ('FST_5', models.CharField(blank=True, max_length=50)),
                ('FST_6', models.CharField(blank=True, max_length=50)),
                ('FST_7', models.CharField(blank=True, max_length=50)),
                ('FST_8', models.CharField(blank=True, max_length=50)),
                ('FST_9', models.CharField(blank=True, max_length=50)),
                ('FST_10', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_master',
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
                ('ST_1', models.CharField(blank=True, max_length=50)),
                ('ST_2', models.CharField(blank=True, max_length=50)),
                ('DTM_1', models.CharField(blank=True, max_length=50)),
                ('DTM_2', models.CharField(blank=True, max_length=50)),
                ('DTM_3', models.CharField(blank=True, max_length=50)),
                ('UIT_1', models.CharField(blank=True, max_length=50)),
                ('UIT_2', models.CharField(blank=True, max_length=50)),
                ('UIT_3', models.CharField(blank=True, max_length=50)),
                ('REF_1', models.CharField(blank=True, max_length=50)),
                ('REF_2', models.CharField(blank=True, max_length=50)),
                ('PER_1', models.CharField(blank=True, max_length=50)),
                ('PER_2', models.CharField(blank=True, max_length=50)),
                ('PER_3', models.CharField(blank=True, max_length=50)),
                ('PER_4', models.CharField(blank=True, max_length=50)),
                ('SHP_1', models.CharField(blank=True, max_length=50)),
                ('SHP_2', models.CharField(blank=True, max_length=50)),
                ('SHP_3', models.CharField(blank=True, max_length=50)),
                ('SHP_4', models.CharField(blank=True, max_length=50)),
                ('SHP_5', models.CharField(blank=True, max_length=50)),
                ('SHP_6', models.CharField(blank=True, max_length=50)),
                ('SHP_7', models.CharField(blank=True, max_length=50)),
                ('SDP_1', models.CharField(blank=True, max_length=50)),
                ('SDP_2', models.CharField(blank=True, max_length=50)),
                ('CT_1', models.CharField(blank=True, max_length=50)),
                ('CT_2', models.CharField(blank=True, max_length=50)),
                ('SE_1', models.CharField(blank=True, max_length=50)),
                ('SE_2', models.CharField(blank=True, max_length=50)),
                ('GE_1', models.CharField(blank=True, max_length=50)),
                ('GE_2', models.CharField(blank=True, max_length=50)),
                ('IEA_1', models.CharField(blank=True, max_length=50)),
                ('IEA_2', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_N',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_0', models.CharField(blank=True, max_length=50)),
                ('N_1', models.CharField(blank=True, max_length=50)),
                ('N_2', models.CharField(blank=True, max_length=50)),
                ('N_3', models.CharField(blank=True, max_length=50)),
                ('N_4', models.CharField(blank=True, max_length=50)),
                ('N3_0', models.CharField(blank=True, max_length=50)),
                ('N3_1', models.CharField(blank=True, max_length=50)),
                ('N4_0', models.CharField(blank=True, max_length=50)),
                ('N4_1', models.CharField(blank=True, max_length=50)),
                ('N4_2', models.CharField(blank=True, max_length=50)),
                ('N4_3', models.CharField(blank=True, max_length=50)),
                ('prim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master')),
            ],
        ),
        migrations.CreateModel(
            name='data_segments_SHP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHP_1', models.CharField(blank=True, max_length=50)),
                ('SHP_2', models.CharField(blank=True, max_length=50)),
                ('SHP_3', models.CharField(blank=True, max_length=50)),
                ('SHP_4', models.CharField(blank=True, max_length=50)),
                ('SHP_5', models.CharField(blank=True, max_length=50)),
                ('SHP_6', models.CharField(blank=True, max_length=50)),
                ('SHP_7', models.CharField(blank=True, max_length=50)),
                ('prim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master')),
            ],
        ),
        migrations.CreateModel(
            name='edi_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edi_file', models.FileField(upload_to='edi/', validators=[data_mining.validators.file_size])),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='data_segments_master',
            name='edi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.edi_address'),
        ),
        migrations.AddField(
            model_name='data_segments_fst',
            name='prim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
        migrations.AddField(
            model_name='data_segments_bss',
            name='prim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
        migrations.AddField(
            model_name='data_segments_bfr',
            name='prim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
        migrations.AddField(
            model_name='data_segments_ath',
            name='prim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
        migrations.AddField(
            model_name='data_segments_862lin',
            name='prim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
        migrations.AddField(
            model_name='data_segments_830lin',
            name='prim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_mining.data_segments_master'),
        ),
    ]

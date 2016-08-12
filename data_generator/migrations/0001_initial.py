# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Generator_Hierarchial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HL01', models.CharField(blank=True, max_length=50)),
                ('HL02', models.CharField(blank=True, max_length=50)),
                ('HL03', models.CharField(blank=True, max_length=50)),
                ('CLD01', models.CharField(blank=True, max_length=50)),
                ('CLD02', models.CharField(blank=True, max_length=50)),
                ('CLD03', models.CharField(blank=True, max_length=50)),
                ('MEA01', models.CharField(blank=True, max_length=50)),
                ('MEA02', models.CharField(blank=True, max_length=50)),
                ('MEA03', models.CharField(blank=True, max_length=50)),
                ('MEA04', models.CharField(blank=True, max_length=50)),
                ('MEA201', models.CharField(blank=True, max_length=50)),
                ('MEA202', models.CharField(blank=True, max_length=50)),
                ('MEA203', models.CharField(blank=True, max_length=50)),
                ('MEA204', models.CharField(blank=True, max_length=50)),
                ('MEA301', models.CharField(blank=True, max_length=50)),
                ('MEA302', models.CharField(blank=True, max_length=50)),
                ('MEA303', models.CharField(blank=True, max_length=50)),
                ('MEA304', models.CharField(blank=True, max_length=50)),
                ('MEA401', models.CharField(blank=True, max_length=50)),
                ('MEA402', models.CharField(blank=True, max_length=50)),
                ('MEA403', models.CharField(blank=True, max_length=50)),
                ('MEA404', models.CharField(blank=True, max_length=50)),
                ('LIN01', models.CharField(blank=True, max_length=50)),
                ('LIN02', models.CharField(blank=True, max_length=50)),
                ('LIN03', models.CharField(blank=True, max_length=50)),
                ('SN101', models.CharField(blank=True, max_length=50)),
                ('SN102', models.CharField(blank=True, max_length=50)),
                ('SN103', models.CharField(blank=True, max_length=50)),
                ('SN104', models.CharField(blank=True, max_length=50)),
                ('PRF01', models.CharField(blank=True, max_length=50)),
                ('REF101', models.CharField(blank=True, max_length=50)),
                ('REF102', models.CharField(blank=True, max_length=50)),
                ('REF201', models.CharField(blank=True, max_length=50)),
                ('REF202', models.CharField(blank=True, max_length=50)),
                ('REF_CLD101', models.CharField(blank=True, max_length=50)),
                ('REF_CLD102', models.CharField(blank=True, max_length=50)),
                ('REF_CLD201', models.CharField(blank=True, max_length=50)),
                ('REF_CLD202', models.CharField(blank=True, max_length=50)),
                ('REF_CLD301', models.CharField(blank=True, max_length=50)),
                ('REF_CLD302', models.CharField(blank=True, max_length=50)),
                ('REF_CLD401', models.CharField(blank=True, max_length=50)),
                ('REF_CLD402', models.CharField(blank=True, max_length=50)),
                ('REF_ITEM101', models.CharField(blank=True, max_length=50)),
                ('REF_ITEM102', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Generator_Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLIENT', models.CharField(blank=True, max_length=50)),
                ('NAME', models.CharField(blank=True, max_length=50)),
                ('PREFIX_CLIENT', models.CharField(blank=True, max_length=50)),
                ('PREFIX_NAME', models.CharField(blank=True, max_length=50)),
                ('ST01', models.CharField(blank=True, max_length=50)),
                ('ST02', models.CharField(blank=True, max_length=50)),
                ('BST01', models.CharField(blank=True, max_length=50)),
                ('BST02', models.CharField(blank=True, max_length=50)),
                ('BST03', models.CharField(blank=True, max_length=50)),
                ('BST04', models.CharField(blank=True, max_length=50)),
                ('DTM01', models.CharField(blank=True, max_length=50)),
                ('DTM02', models.CharField(blank=True, max_length=50)),
                ('DTM03', models.CharField(blank=True, max_length=50)),
                ('DTM04', models.CharField(blank=True, max_length=50)),
                ('DTM05', models.CharField(blank=True, max_length=50)),
                ('MEA01', models.CharField(blank=True, max_length=50)),
                ('MEA02', models.CharField(blank=True, max_length=50)),
                ('MEA03', models.CharField(blank=True, max_length=50)),
                ('MEA04', models.CharField(blank=True, max_length=50)),
                ('TD101', models.CharField(blank=True, max_length=50)),
                ('TD102', models.CharField(blank=True, max_length=50)),
                ('TD501', models.CharField(blank=True, max_length=50)),
                ('TD502', models.CharField(blank=True, max_length=50)),
                ('TD503', models.CharField(blank=True, max_length=50)),
                ('TD504', models.CharField(blank=True, max_length=50)),
                ('TD505', models.CharField(blank=True, max_length=50)),
                ('TD506', models.CharField(blank=True, max_length=50)),
                ('TD507', models.CharField(blank=True, max_length=50)),
                ('TD508', models.CharField(blank=True, max_length=50)),
                ('TD301', models.CharField(blank=True, max_length=50)),
                ('TD302', models.CharField(blank=True, max_length=50)),
                ('TD303', models.CharField(blank=True, max_length=50)),
                ('TD401', models.CharField(blank=True, max_length=50)),
                ('TD402', models.CharField(blank=True, max_length=50)),
                ('TD403', models.CharField(blank=True, max_length=50)),
                ('TD404', models.CharField(blank=True, max_length=50)),
                ('TD405', models.CharField(blank=True, max_length=50)),
                ('REF01', models.CharField(blank=True, max_length=50)),
                ('REF02', models.CharField(blank=True, max_length=50)),
                ('ETD01', models.CharField(blank=True, max_length=50)),
                ('ETD02', models.CharField(blank=True, max_length=50)),
                ('ETD03', models.CharField(blank=True, max_length=50)),
                ('CTT01', models.CharField(blank=True, max_length=50)),
                ('CTT02', models.CharField(blank=True, max_length=50)),
                ('SE01', models.CharField(blank=True, max_length=50)),
                ('SE02', models.CharField(blank=True, max_length=50)),
                ('N101', models.CharField(blank=True, max_length=50)),
                ('N102', models.CharField(blank=True, max_length=50)),
                ('N103', models.CharField(blank=True, max_length=50)),
                ('N104', models.CharField(blank=True, max_length=50)),
                ('N201', models.CharField(blank=True, max_length=50)),
                ('N202', models.CharField(blank=True, max_length=50)),
                ('N203', models.CharField(blank=True, max_length=50)),
                ('N204', models.CharField(blank=True, max_length=50)),
                ('N301', models.CharField(blank=True, max_length=50)),
                ('N302', models.CharField(blank=True, max_length=50)),
                ('N303', models.CharField(blank=True, max_length=50)),
                ('N304', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Generator_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N101', models.CharField(blank=True, max_length=50)),
                ('N102', models.CharField(blank=True, max_length=50)),
                ('N103', models.CharField(blank=True, max_length=50)),
                ('N104', models.CharField(blank=True, max_length=50)),
                ('PRIM', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Master')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Generator_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LIN01', models.CharField(blank=True, max_length=50)),
                ('LIN02', models.CharField(blank=True, max_length=50)),
                ('LIN03', models.CharField(blank=True, max_length=50)),
                ('SN101', models.CharField(blank=True, max_length=50)),
                ('SN102', models.CharField(blank=True, max_length=50)),
                ('SN103', models.CharField(blank=True, max_length=50)),
                ('SN104', models.CharField(blank=True, max_length=50)),
                ('PRF01', models.CharField(blank=True, max_length=50)),
                ('REF101', models.CharField(blank=True, max_length=50)),
                ('REF102', models.CharField(blank=True, max_length=50)),
                ('REF201', models.CharField(blank=True, max_length=50)),
                ('REF202', models.CharField(blank=True, max_length=50)),
                ('PRIM', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Master')),
            ],
        ),
        migrations.AddField(
            model_name='data_generator_hierarchial',
            name='PRIM',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Master'),
        ),
    ]

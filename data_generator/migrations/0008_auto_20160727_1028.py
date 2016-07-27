# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-27 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_generator', '0007_auto_20160726_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Generator_I_CLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLD01', models.CharField(blank=True, max_length=50)),
                ('CLD02', models.CharField(blank=True, max_length=50)),
                ('CLD03', models.CharField(blank=True, max_length=50)),
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
                ('PRIM', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Hierarchial')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Generator_Order_REF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REF01', models.CharField(blank=True, max_length=50)),
                ('REF02', models.CharField(blank=True, max_length=50)),
                ('PRIM', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Hierarchial')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Generator_REFI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REF01', models.CharField(max_length=50)),
                ('REF02', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='data_generator_o_ref',
            name='PRIM',
        ),
        migrations.RemoveField(
            model_name='data_generator_ref',
            name='PRIM',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='CLD01',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='CLD02',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='CLD03',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='LIN01',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='LIN02',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='LIN03',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='SN101',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='SN102',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='SN103',
        ),
        migrations.RemoveField(
            model_name='data_generator_master',
            name='SN104',
        ),
        migrations.AlterField(
            model_name='data_generator_i_mea',
            name='PRIM',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Hierarchial'),
        ),
        migrations.AlterField(
            model_name='data_generator_i_ref',
            name='PRIM',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Hierarchial'),
        ),
        migrations.AlterField(
            model_name='data_generator_name',
            name='PRIM',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Master'),
        ),
        migrations.DeleteModel(
            name='Data_Generator_O_REF',
        ),
        migrations.DeleteModel(
            name='Data_Generator_REF',
        ),
        migrations.AddField(
            model_name='data_generator_refi',
            name='PRIM',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='data_generator.Data_Generator_Master'),
        ),
    ]

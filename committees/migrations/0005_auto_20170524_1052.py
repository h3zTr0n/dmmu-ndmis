# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0004_auto_20170524_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliefmaizedistribution',
            name='first_50_percent_chq_num',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='1st 50% CHQ #'),
        ),
        migrations.AlterField(
            model_name='reliefmaizedistribution',
            name='second_50_percent_chq_num',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='2st 50% CHQ #'),
        ),
    ]

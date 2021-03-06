# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaizeRequisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date Prepared')),
                ('to', models.CharField(max_length=255, verbose_name='To')),
                ('source', models.CharField(max_length=255, verbose_name='Source(Place)')),
                ('req_num', models.CharField(max_length=255, verbose_name='Requisition Number')),
                ('destination', models.CharField(max_length=255, verbose_name='Destination(Place)')),
                ('item_descr', models.CharField(max_length=355, verbose_name='Item Description')),
                ('qty', models.CharField(max_length=255, verbose_name='Quantity (Qty)')),
                ('unit', models.CharField(max_length=255, verbose_name='Unit')),
                ('stock_code', models.CharField(max_length=255, verbose_name='Stock Code')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('prepared_by', models.CharField(max_length=255, verbose_name='Prepared by: (name):')),
                ('prepared_by_signature_status', models.BooleanField(default=0, verbose_name='Prepared by: (signature(signed/pending))')),
                ('approved_by', models.CharField(max_length=255, verbose_name='Approved by: (name):')),
                ('approved_by_signature_status', models.BooleanField(default=0, verbose_name='Approved by: (signature(signed/pending))')),
                ('authorised_by', models.CharField(max_length=255, verbose_name='Authorised by: (name):')),
                ('authorised_by_signature_status', models.BooleanField(default=0, verbose_name='Authorised by: (signature(signed/pending))')),
            ],
            options={
                'verbose_name': 'MAIZE REQUISITION',
                'verbose_name_plural': 'MAIZE REQUISITIONS',
            },
        ),
    ]

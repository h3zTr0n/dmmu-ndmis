# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirportAirdromeAirstrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, verbose_name='Location ')),
                ('size', models.CharField(max_length=255, verbose_name='Size')),
                ('_type', models.CharField(choices=[('AP', 'Airport'), ('AD', 'Airdrome'), ('AS', 'Airstripe')], max_length=255, verbose_name='Type')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Latitude')),
                ('length', models.CharField(blank=True, max_length=255, null=True, verbose_name='Length')),
                ('tonnage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tonnage')),
                ('limitation', models.TextField(blank=True, null=True, verbose_name='Limitation')),
                ('communication', models.TextField(blank=True, null=True, verbose_name='Communication')),
                ('Elevation', models.TextField(blank=True, null=True, verbose_name='Elevation')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'AIRPORT, AIRDROME AND AIRSTRIPE',
                'verbose_name_plural': 'AIRPORTS, AIRDROMES AND AIRSTRIPES',
            },
        ),
        migrations.CreateModel(
            name='DisasterEmergencyBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Building Name')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('size', models.CharField(max_length=255, verbose_name='Building Size')),
                ('emergency_usage', models.CharField(choices=[('ES', 'Emergency Shelter'), ('HF', 'Health facility')], max_length=255, verbose_name='Type of use in Emergency')),
            ],
        ),
        migrations.CreateModel(
            name='DisasterEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Equipment Name')),
                ('number', models.CharField(blank=255, max_length=255, null=True, verbose_name='Number of Equipments (How many)')),
                ('description', models.TextField(blank=255, null=True, verbose_name='Notes On Equipment')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Latitude')),
                ('_type', models.CharField(blank=True, choices=[('V', 'Vehicle'), ('A', 'Aircraft'), ('T', 'Tractor'), ('O', 'Other')], max_length=255, null=True, verbose_name='Equipment Type')),
                ('capacity', models.CharField(blank=True, max_length=255, null=True, verbose_name='Equipment Capacity')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'DISASTER MANAGEMENT EQUIPMENT',
                'verbose_name_plural': 'DISASTER MANAGEMENT EQUIPMENTS',
            },
        ),
        migrations.CreateModel(
            name='FireFightingStationsAndUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Faility Name')),
                ('facility_type', models.CharField(choices=[('FFS', 'Fire Fighting Station'), ('FFU', 'Fire Fighting Unit')], max_length=255, verbose_name='Facility Type')),
                ('street_address', models.TextField(verbose_name='Street Adress')),
                ('province', models.CharField(blank=True, max_length=255, null=True, verbose_name='Province')),
                ('postal_code', models.CharField(default=10101, max_length=255, verbose_name='Postal code')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Longitude')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact')),
                ('phone1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone 1')),
                ('phone2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website URL')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes/Comments')),
            ],
            options={
                'verbose_name': 'FIREFIGHTING SATION AND UNIT',
                'verbose_name_plural': 'FIREFIGHTING STATIONS AND UNITS',
            },
        ),
        migrations.CreateModel(
            name='GovtHeadsAddressBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_name', models.CharField(max_length=255, verbose_name="Head's Name")),
                ('work', models.CharField(max_length=255, verbose_name='Work Phone')),
                ('cell', models.CharField(max_length=255, verbose_name='Cell Phone')),
                ('home', models.CharField(blank=True, max_length=255, null=True, verbose_name='Home phone')),
                ('related_office', models.CharField(choices=[('P', 'Provincial Office'), ('D', 'District Office')], max_length=255, verbose_name='Belongs to')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('birthday', models.DateField(max_length=255, verbose_name='Birthday')),
                ('address', models.TextField(max_length=255, verbose_name='Resident Adress')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('province', models.CharField(max_length=255, verbose_name='Province')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('postal_code', models.CharField(default=10101, max_length=255, verbose_name='Postal Code')),
                ('notes', models.TextField(help_text='Enter Notes under this column', verbose_name='Note')),
            ],
            options={
                'verbose_name': 'GOVERNMENT HEADS ADDRESSBOOK',
                'verbose_name_plural': 'GOVERNMENT HEADS ADDRESSBOOKS',
            },
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Health Faility Name')),
                ('health_facility', models.CharField(max_length=255, verbose_name='Health Facility')),
                ('facility_type', models.CharField(choices=[('H', 'Hospital'), ('C', 'Clinic'), ('RHC', 'Rural Health Centre'), ('UHC', 'Urban Health Centre')], max_length=255, verbose_name='Health Facility Type')),
                ('street_address', models.TextField(verbose_name='Street Adress')),
                ('province', models.CharField(blank=True, max_length=255, null=True, verbose_name='Province')),
                ('postal_code', models.CharField(default=10101, max_length=255, verbose_name='Postal code')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Longitude')),
                ('opening_times', models.CharField(blank=True, max_length=255, null=True, verbose_name='Opening Times')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact')),
                ('phone1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone 1')),
                ('phone2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website URL')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes/Comments')),
            ],
        ),
        migrations.CreateModel(
            name='HealthPractitionerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Practitioner's Name")),
                ('job_title', models.CharField(max_length=255, verbose_name='Job Title')),
                ('department', models.CharField(max_length=255, verbose_name='Department')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Comments/Remarks')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.HealthFacility')),
            ],
            options={
                'verbose_name': 'HEALTH PRACTITIONER DETAILS',
                'verbose_name_plural': 'HEALTH PRACTIONERS DETAILS',
            },
        ),
        migrations.CreateModel(
            name='LearningInstitutionAdressesBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Institution Name')),
                ('_type', models.CharField(choices=[('BI', 'Basic Institution'), ('PI', 'Primary Institution'), ('SI', 'Secondary Institution'), ('TI', 'Tertiary Institution')], max_length=255, verbose_name='Institution/School Type')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('head_name', models.CharField(max_length=255, verbose_name='Institution Head Name')),
                ('address', models.TextField(verbose_name="Head's Address")),
            ],
            options={
                'verbose_name': 'LEARNING INSTITUTIONS ADDRESS BOOK',
                'verbose_name_plural': 'LEARNING INSTITUTIONS ADDRESS BOOKS',
            },
        ),
    ]
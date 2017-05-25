from __future__ import absolute_import
from django.contrib import admin

from .models import GovtHeadsAddressBook, LearningInstitutionAdressesBook, HealthFacility, HealthPractitionerDetails, FireFightingStationsAndUnits, DisasterEmergencyBuilding, AirportAirdromeAirstrip,DisasterEquipment
# Register your models here.
class GovtHeadsAddressBookAdmin(admin.ModelAdmin):
    list_display = ['head_name', 'work', 'cell', 'home', 'related_office', 'email', 'province', 'postal_code']
    search_fields = ['head_name', 'cell', 'email', 'province',]
    list_filter = ('head_name', 'cell', 'email', 'province',)
admin.site.register(GovtHeadsAddressBook, GovtHeadsAddressBookAdmin)

class LearningInstitutionAdressesBookAdmin(admin.ModelAdmin):
    list_display = ['name', '_type', 'location', 'head_name', 'address']
    search_fields = ['name', '_type', 'location', 'head_name', 'address',]
    list_filter = ('_type', 'location',)
admin.site.register(LearningInstitutionAdressesBook, LearningInstitutionAdressesBookAdmin)

class HealthFacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'facility_type', 'province', 'opening_times', 'phone1', 'email', 'website']
    search_fields = ['name', 'facility_type', 'province',]
    list_filter = ('name', 'facility_type', 'province',)
admin.site.register(HealthFacility, HealthFacilityAdmin)

class HealthPractitionerDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'department', 'start_date', 'facility']
    search_fields = ['name', 'job_title', 'department', 'start_date',]
    list_filter = ('job_title', 'department', 'start_date',)
admin.site.register(HealthPractitionerDetails, HealthPractitionerDetailsAdmin)

class FireFightingStationsAndUnitsAdmin(admin.ModelAdmin):
    list_display = ['name', 'facility_type', 'province', 'phone1', 'email', 'website']
    search_fields = ['name', 'facility_type', 'province', 'phone1', 'email', 'website',]
    list_filter = ('name', 'facility_type', 'province',)
admin.site.register(FireFightingStationsAndUnits, FireFightingStationsAndUnitsAdmin)

class DisasterEmergencyBuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'size', 'emergency_usage']
    search_fields = ['name', 'location', 'size', 'emergency_usage',]
    list_filter = ('name', 'location', 'size', 'emergency_usage',)
admin.site.register(DisasterEmergencyBuilding, DisasterEmergencyBuildingAdmin)

class AirportAirdromeAirstripAdmin(admin.ModelAdmin):
    list_display = ['location', 'size', '_type', 'tonnage', 'Elevation']
    search_fields = ['location', 'size', '_type', 'tonnage', 'Elevation',]
    list_filter = ('location', 'size', '_type',)
admin.site.register(AirportAirdromeAirstrip, AirportAirdromeAirstripAdmin)

class DisasterEquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'location', '_type', 'capacity']
    search_fields = ['name', 'number', 'location', '_type', 'capacity',]
    list_filter = ('name', 'number', 'location', '_type', 'capacity',)
admin.site.register(DisasterEquipment, DisasterEquipmentAdmin)

from __future__ import absolute_import

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin

from .models import (GovtHeadsAddressBook, LearningInstitutionAdressesBook,
                    DisasterEmergencyBuilding, AirportAirdromeAirstrip,DisasterEquipment,
                    HealthFacility, HealthPractitionerDetails, FireFightingStationsAndUnits)

class GovtHeadsAddressBookResource(resources.ModelResource):
    class Meta:
        model = GovtHeadsAddressBook

class GovtHeadsAddressBookAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['head_name', 'work', 'cell', 'home', 'related_office', 'email', 'province', 'postal_code']
    search_fields = ['head_name', 'cell', 'email', 'province',]
    list_filter = ('head_name', 'cell', 'email', 'province',)
    resource_class = GovtHeadsAddressBookResource
admin.site.register(GovtHeadsAddressBook, GovtHeadsAddressBookAdmin)

class LearningInstitutionAdressesBookResource(resources.ModelResource):
    class Meta:
        model = LearningInstitutionAdressesBook

class LearningInstitutionAdressesBookAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', '_type', 'location', 'head_name', 'address']
    search_fields = ['name', '_type', 'location', 'head_name', 'address',]
    list_filter = ('_type', 'location',)
    resource_class = LearningInstitutionAdressesBookResource
admin.site.register(LearningInstitutionAdressesBook, LearningInstitutionAdressesBookAdmin)

class HealthFacilityResource(resources.ModelResource):
    class Meta:
        model = HealthFacility

class HealthFacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'facility_type', 'province', 'opening_times', 'phone1', 'email', 'website']
    search_fields = ['name', 'facility_type', 'province',]
    list_filter = ('name', 'facility_type', 'province',)
    resource_class = HealthFacilityResource
admin.site.register(HealthFacility, HealthFacilityAdmin)

class HealthPractitionerDetailsResource(resources.ModelResource):
    class Meta:
        model = HealthPractitionerDetails

class HealthPractitionerDetailsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'job_title', 'department', 'start_date', 'facility']
    search_fields = ['name', 'job_title', 'department', 'start_date',]
    list_filter = ('job_title', 'department', 'start_date',)
    resource_class = HealthPractitionerDetailsResource
admin.site.register(HealthPractitionerDetails, HealthPractitionerDetailsAdmin)

class FireFightingStationsAndUnitsResource(resources.ModelResource):
    class Meta:
        model = FireFightingStationsAndUnits

class FireFightingStationsAndUnitsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'facility_type', 'province', 'phone1', 'email', 'website']
    search_fields = ['name', 'facility_type', 'province', 'phone1', 'email', 'website',]
    list_filter = ('name', 'facility_type', 'province',)
    resource_class = FireFightingStationsAndUnitsResource
admin.site.register(FireFightingStationsAndUnits, FireFightingStationsAndUnitsAdmin)

class DisasterEquipmentResource(resources.ModelResource):
    class Meta:
        model = DisasterEquipment

class DisasterEmergencyBuildingAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'location', 'size', 'emergency_usage']
    search_fields = ['name', 'location', 'size', 'emergency_usage',]
    list_filter = ('name', 'location', 'size', 'emergency_usage',)
    resource_class = DisasterEquipmentResource
admin.site.register(DisasterEmergencyBuilding, DisasterEmergencyBuildingAdmin)

class AirportAirdromeAirstripResource(resources.ModelResource):
    class Meta:
        model = AirportAirdromeAirstrip

class AirportAirdromeAirstripAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['location', 'size', '_type', 'tonnage', 'Elevation']
    search_fields = ['location', 'size', '_type', 'tonnage', 'Elevation',]
    list_filter = ('location', 'size', '_type',)
    resource_class = AirportAirdromeAirstripResource
admin.site.register(AirportAirdromeAirstrip, AirportAirdromeAirstripAdmin)

class DisasterEquipmentResource(resources.ModelResource):
    class Meta:
        model = DisasterEquipment

class DisasterEquipmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'number', 'location', '_type', 'capacity']
    search_fields = ['name', 'number', 'location', '_type', 'capacity',]
    list_filter = ('name', 'number', 'location', '_type', 'capacity',)
    resource_class = DisasterEquipmentResource
admin.site.register(DisasterEquipment, DisasterEquipmentAdmin)

from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin

from .models import (OrganizationType, OrganizationSector, OrganizationOfficeType,
                    Organization, Facility, StaffMember, Asset, ProgrammeStatusChoices,
                    Programme, Department, Person, Skill, Competency, StaffSkills, JobTitleCatalog
                    )
class OrganizationTypeResource(resources.ModelResource):
    class Meta:
        model = OrganizationType

class OrganizationTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OrganizationTypeResource
admin.site.register(OrganizationType, OrganizationTypeAdmin)

class OrganizationSectorResource(resources.ModelResource):
    class Meta:
        model = OrganizationSector

class OrganizationSectorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OrganizationSectorResource
admin.site.register(OrganizationSector, OrganizationTypeAdmin)

class OrganizationOfficeTypeResource(resources.ModelResource):
    class Meta:
        model = OrganizationOfficeType

class OrganizationOfficeTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OrganizationOfficeTypeResource
admin.site.register(OrganizationOfficeType, OrganizationOfficeTypeAdmin)

class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization

class OrganizationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OrganizationResource
admin.site.register(Organization, OrganizationAdmin)

class FacilityResource(resources.ModelResource):
    class Meta:
        model = Facility

class FacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FacilityResource
admin.site.register(Facility, FacilityAdmin)

class AssetResource(resources.ModelResource):
    class Meta:
        model = Asset

class AssetAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AssetResource
admin.site.register(Asset, AssetAdmin)

class ProgrammeStatusChoicesResource(resources.ModelResource):
    class Meta:
        model = ProgrammeStatusChoices

class ProgrammeStatusChoicesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProgrammeStatusChoicesResource
admin.site.register(ProgrammeStatusChoices, ProgrammeStatusChoicesAdmin)

class ProgramResource(resources.ModelResource):
    class Meta:
        model = Programme

class ProgrammeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProgramResource
admin.site.register(Programme, ProgrammeAdmin)

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DepartmentResource
admin.site.register(Department, DepartmentAdmin)

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class PersonAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PersonResource
admin.site.register(Person, PersonAdmin)

class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill

class SkillAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SkillResource
admin.site.register(Skill, SkillAdmin)

class CompetencyResource(resources.ModelResource):
    class Meta:
        model = Competency

class CompetencyAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CompetencyResource
admin.site.register(Competency, CompetencyAdmin)

class StaffSkillsResource(resources.ModelResource):
    class Meta:
        model = StaffSkills

class StaffSkillsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StaffSkillsResource
admin.site.register(StaffSkills, StaffSkillsAdmin)

class JobTitleCatalogResource(resources.ModelResource):
    class Meta:
        model = JobTitleCatalog

class JobTitleCatalogAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = JobTitleCatalogResource

# admin.site.register(StaffMember)StaffMember
admin.site.register(JobTitleCatalog, JobTitleCatalogAdmin)

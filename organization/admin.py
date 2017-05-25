from __future__ import absolute_import
from django.contrib import admin

from .models import OrganizationType, OrganizationSector, OrganizationOfficeType, Organization, Facility, StaffMember, Asset, ProgrammeStatusChoices, Programme, Department, Person, Skill, Competency, StaffSkills, JobTitleCatalog
admin.site.register(OrganizationType)
admin.site.register(OrganizationSector)
admin.site.register(OrganizationOfficeType)
admin.site.register(Organization)
admin.site.register(Facility)
# admin.site.register(StaffMember)StaffMember
admin.site.register(Asset)
admin.site.register(ProgrammeStatusChoices)
admin.site.register(Programme)
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(Competency)
admin.site.register(StaffSkills)
admin.site.register(JobTitleCatalog)

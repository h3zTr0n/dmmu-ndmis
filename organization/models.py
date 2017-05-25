from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# from ..organization import models as organization_models

class OrganizationType(models.Model):
    name = models.CharField(_("Organization Type Name"), max_length=255)
    created = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.name

class OrganizationSector(models.Model):
    name = models.CharField(_("Organization Sector name"), max_length=255)
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self. name

class OrganizationOfficeType(models.Model):
    name = models.CharField(_("Organization Office Name"), max_length=255)
    code = models.CharField(_("Organization Office Code"), max_length=255)
    _type = models.CharField(_("Organization Office Type"), max_length=255)
    Street_address = models.CharField(_("Organziation Street Adress"), max_length=255)
    postcode = models.CharField(_("Organization POst Code"), max_length=255)
    latitude = models.CharField(_("Organization Office Latitude"), max_length=255)
    longitude = models.CharField(_("Organization Office Longitude"), max_length=255)
    Phone_1 = models.CharField(_("Phone line 1"), max_length=255)
    Phone_2 = models.CharField(_("Phone line 2"), max_length=255)
    email = models.EmailField(_("Office Email Address"))
    remarks = models.TextField(_("Remarks or Comments"))

    def __unicode__(self):
        return self.name
#
# class OrganizationOffice(models.Model):
#     name = models.CharField(_("Organzation Office Name"), max_length=255)
#     office_type = models.CharField()
#
COUNTRY_CHOICES = (
        ("ZM", "Zambia"),
        ("USA", "United States of America"),
    )
class Organization(models.Model):
    name = models.CharField(_("Name"),max_length=255)
    acronym = models.CharField(_("Acronym"), max_length=255)
    _type = models.ForeignKey(OrganizationType)
    country = models.CharField(_("Home Country"), max_length=255, choices=COUNTRY_CHOICES)
    phone = models.CharField(_("Phone Number"), max_length=255)
    website = models.URLField(_("Website URL"))
    Year = models.DateField(_("Date Organization was Founded"), blank=True,auto_now=False)
    # logo = models.ImageField(_("Organization Logo"))
    remarks = models.TextField(_("Remarks or Comments"))
    # offices = models.ForeignKey(organization_models.OrganizationOffice, _("Offices"))

class Facility(models.Model):
    name = models.CharField(_("Facility Name"), max_length=255)
    # facility = models.CharField(_("Facility"), max_length=255, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.name

GENDER_CHOICES = (
    ('M', "Male"),
    ('F', 'Female'),
)
STAFF_STATUS = (
    ("A","Active"),
    ("R", "Resigned"),
    ("T", "Terminated"),
    ("D", "Died"),
)
class StaffMember(models.CharField):
    facility = models.CharField(_("Facility"), max_length=255)
    name = models.CharField(_("Staff Name"), max_length=255)
    date_of_birth = models.DateField(_("Date Of Birth"), null=True, blank=True)
    gender = models.CharField("Gender", choices=GENDER_CHOICES, max_length=255)
    phone = models.CharField(_("Mobile Phone"), max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"))
    job_title = models.CharField(_("Job Title"), max_length=255)
    department_unit = models.CharField(_("Department/Unit"), max_length=255)
    start_date = models.DateField(_("Start Date"),auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False)
    status = models.CharField(_("Status"), max_length=255, choices=STAFF_STATUS)
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.name

ASSET_TYPE_CHOICES= (
    ("V", "Vehicle"),
    ("O", "Other"),
)

CURRENCY_CHOICES = (
    ("ZMK", "ZMK"),
    ("USD", "USD"),
    ("GBP", "GBP"),
    ("EUR", "EUR"),
)

class Asset(models.Model):
    asset_number = models.CharField(_("Asset Number"), max_length=255)
    _type = models.CharField(_("Asset Type"), max_length=255, choices=ASSET_TYPE_CHOICES)
    item = models.CharField(_("Item"), max_length=255)
    facility = models.ForeignKey(Facility)
    serial_number = models.CharField(_("Serial Number"), max_length=255)
    supplier_donor = models.ForeignKey(Organization)
    purchase_date = models.DateField(_("Purchase Date"), auto_now=False)
    purchase_price = models.CharField(_("Purchase Price"), max_length=255, null=True, blank=True)
    currency = models.CharField(_("Currency"), max_length=255, choices=CURRENCY_CHOICES)
    condition = models.CharField(_("Condition"), help_text=_("e.g good, bad etc"), max_length=255)
    comments = models.TextField(_("Comments on Asset"))

    def __unicode__(self):
        return self.asset_number

class ProgrammeStatusChoices(models.Model):
    name = models.CharField(_("Programe Status Name"), help_text=_("e.g pending, active etc"), max_length=255)
    comments = models.TextField(_("Comments"))

    def __unicode__(self):
        return self.name

class Programme(models.Model):
    name = models.CharField(_("Programme Name"), max_length=255)
    Short_title = models.CharField(_("Short Title / ID"), max_length=255)
    description = models.TextField(_("Description"))
    status = models.ForeignKey(ProgrammeStatusChoices)
    start_date = models.DateField(_("Start Date"), auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False)
    # contact_person = models.ForeignKey(StaffMember)
    comments = models.TextField(_("Comments"))

    def __unicode__(self):
        return self.name
# class StaffAndVolunteers(models.Model):
#     name = models.CharField("Staff Name", max_length=255)
#     job_title = models.CharField("Job Title", max_length=255)
#     department_unit = models.CharField("Department/Unit", max_length=255)
#     contact = models.CharField()

class Department(models.Model):
    name = models.CharField(_("Department Name"), max_length=255)
    organization = models.ForeignKey(Organization)
    description = models.TextField(_("Description"))

    def __unicode__(Self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_name = models.CharField(_("Middle Name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True, blank=True)
    initials = models.CharField(_("Initials"), max_length=255, null=True, blank=True)
    gender = models.CharField(_("Gender"), max_length=255, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(_("Date of birth"), auto_now=False)
    remarks = models.TextField(_("Remarks"), null=True, blank=True)
    # organization = models.ForeignKey(Organization, _("Organization"))

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    comments = models.TextField(_("Comments"))

    def __unicode__(Self):
        return self.name

class Competency(models.Model):
    name = models.CharField(_("Competency Name"), max_length=255)
    priority = models.IntegerField(_("Priority"), help_text=_("Priority from 1 to 9, 1 is most prefferd."))

    def __unicode__(self):
        return self.name

class StaffSkills(models.Model):
    person = models.ForeignKey(Person)
    skill = models.ForeignKey(Skill)
    competency = models.ForeignKey(Competency)
    Organization = models.ForeignKey(Organization)

    def __unicode__(Self):
        return self.person
JOB_TYPE_CHOICES = (
    ("S", "Saff"),
    ("V", "Volunteer"),
    ("B", "Both"),
)
class JobTitleCatalog(models.Model):
    name = models.CharField(_("Job Title"), max_length=255)
    typ = models.CharField(_("Type"), max_length=255, choices=JOB_TYPE_CHOICES)
    description = models.TextField(_("Job Descritpion"))

    def __unicode__(Self):
        return self.name

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

OFFICE_TYPE_CHOICES = (
    ("P", "Provincial Office"),
    ("D", "District Office"),
)

class GovtHeadsAddressBook(models.Model):
    head_name = models.CharField(_("Head's Name"), max_length=255)
    work = models.CharField(_("Work Phone"), max_length=255)
    cell = models.CharField(_("Cell Phone"), max_length=255)
    home = models.CharField(_("Home phone"), max_length=255, null=True, blank=True)
    related_office = models.CharField(_("Belongs to"), max_length=255, choices=OFFICE_TYPE_CHOICES)
    email = models.EmailField(_("Email"), max_length=255)
    birthday = models.DateField(_("Birthday"), max_length=255)
    address = models.TextField(_("Resident Adress"), max_length=255)
    city = models.CharField(_("City"), max_length=255)
    province = models.CharField(_("Province"), max_length=255)
    country = models.CharField(_("Country"), max_length=255)
    postal_code = models.CharField(_("Postal Code"), max_length=255, default=10101)
    notes = models.TextField(_("Note"), help_text=_("Enter Notes under this column"))
    class Meta:
        verbose_name = "GOVERNMENT HEADS ADDRESSBOOK"
        verbose_name_plural = "GOVERNMENT HEADS ADDRESSBOOKS"

    def __unicode__(self):
        return self.name

INSTITUTION_TYPE_CHOICES = (
    ("BI", "Basic Institution"),
    ("PI", "Primary Institution"),
    ("SI", "Secondary Institution"),
    ("TI", "Tertiary Institution"),

)
class LearningInstitutionAdressesBook(models.Model):
    name = models.CharField(_("Institution Name"), max_length=255)
    _type = models.CharField(_("Institution/School Type"), max_length=255, choices=INSTITUTION_TYPE_CHOICES)
    location = models.CharField(_("Location"), max_length=255)
    head_name = models.CharField(_("Institution Head Name"), max_length=255)
    address = models.TextField(_("Head's Address"))
    class Meta:
        verbose_name = "LEARNING INSTITUTIONS ADDRESS BOOK"
        verbose_name_plural = "LEARNING INSTITUTIONS ADDRESS BOOKS"

    def __unicode__(self):
        return self.name

HEALTH_FACILITY_TYPES = (
    ("H", "Hospital"),
    ("C", "Clinic"),
    ("RHC", "Rural Health Centre"),
    ("UHC", "Urban Health Centre"),
)

class HealthFacility(models.Model):
    name = models.CharField(_("Health Faility Name"), max_length=255)
    health_facility = models.CharField(_("Health Facility"), max_length=255)
    facility_type = models.CharField(_("Health Facility Type"), max_length=255, choices=HEALTH_FACILITY_TYPES)
    street_address = models.TextField(_("Street Adress"))
    province = models.CharField(_("Province"), max_length=255, null=True, blank=True)
    postal_code = models.CharField(_("Postal code"), max_length=255, default=10101)
    latitude = models.CharField(_("Latitude"), max_length=255, null=True, blank=True)
    longitude = models.CharField(_("Longitude"), max_length=255, null=True, blank=True)
    opening_times = models.CharField(_("Opening Times"), max_length=255, null=True, blank=True)
    contact = models.CharField(_("Contact"), max_length=255, null=True, blank=True)
    phone1 = models.CharField(_("Phone 1"), max_length=255, null=True, blank=True)
    phone2 = models.CharField(_("Phone 2"), max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    website = models.URLField(_("Website URL"), null=True, blank=True)
    notes = models.TextField(_("Notes/Comments"), null=True, blank=True)
    class Meta:
        verbose_name = "HEALTH FACILITY"
        verbose_name_plural = "HEALTH FACILITIES"

    def __unicode__(self):
        return self.name

class HealthPractitionerDetails(models.Model):
    name = models.CharField(_("Practitioner's Name"), max_length=255)
    job_title = models.CharField(_("Job Title"), max_length=255)
    department = models.CharField(_("Department"), max_length=255)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"), null=True, blank=True)
    remarks = models.TextField(_("Comments/Remarks"), null=True, blank=True)
    facility = models.ForeignKey(HealthFacility)
    class Meta:
        verbose_name = "HEALTH PRACTITIONER DETAILS"
        verbose_name_plural = "HEALTH PRACTIONERS DETAILS"

    def __unicode__(self):
        return self.name

FIREFIGHTING_UNIT_CHOICES = (
    ("FFS", "Fire Fighting Station"),
    ("FFU", "Fire Fighting Unit"),
)
class FireFightingStationsAndUnits(models.Model):
    name = models.CharField(_("Faility Name"), max_length=255)
    facility_type = models.CharField(_("Facility Type"), max_length=255, choices=FIREFIGHTING_UNIT_CHOICES)
    street_address = models.TextField(_("Street Adress"))
    province = models.CharField(_("Province"), max_length=255, null=True, blank=True)
    postal_code = models.CharField(_("Postal code"), max_length=255, default=10101)
    latitude = models.CharField(_("Latitude"), max_length=255, null=True, blank=True)
    longitude = models.CharField(_("Longitude"), max_length=255, null=True, blank=True)
    # opening_times = models.CharField(_("Opening Times"), max_length=255, null=True, blank=True)
    contact = models.CharField(_("Contact"), max_length=255, null=True, blank=True)
    phone1 = models.CharField(_("Phone 1"), max_length=255, null=True, blank=True)
    phone2 = models.CharField(_("Phone 2"), max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    website = models.URLField(_("Website URL"), null=True, blank=True)
    notes = models.TextField(_("Notes/Comments"), null=True, blank=True)
    class Meta:
        verbose_name = "FIREFIGHTING SATION AND UNIT"
        verbose_name_plural = "FIREFIGHTING STATIONS AND UNITS"

    def __unicode__(self):
        return self.name

EMERGENCY_TYPE = (
    ("ES", "Emergency Shelter"),
    ("HF", "Health facility"),
)
class DisasterEmergencyBuilding(models.Model):
    name = models.CharField(_("Building Name"), max_length=255, null=True, blank=True)
    location = models.CharField(_("Location"), max_length=255, null=True, blank=True)
    size = models.CharField(_("Building Size"), max_length=255)
    emergency_usage = models.CharField(_("Type of use in Emergency"), max_length=255, choices=EMERGENCY_TYPE)
    class Meta:
        verbose_name = "DISASTER EMERGENCY BUILDING"
        verbose_name_plural = "DISASTER EMERGENCY BUILDINGS"

    def __unicode__(self):
        return self.name

TYPE = (
    ("AP","Airport"),
    ("AD", "Airdrome"),
    ("AS", "Airstripe"),
)
class AirportAirdromeAirstrip(models.Model):
    location = models.CharField(_("Location "), max_length=255)
    size = models.CharField(_("Size"), max_length=255)
    _type = models.CharField(_("Type"), max_length=255, choices=TYPE)
    longitude = models.CharField(_("Longitude"), max_length=255, null=True, blank=True)
    latitude = models.CharField(_("Latitude"), max_length=255, null=True, blank=True)
    length = models.CharField(_("Length"), max_length=255, null=True, blank=True)
    tonnage = models.CharField(_("Tonnage"), max_length=255, null=True, blank=True)
    limitation = models.TextField(_("Limitation"), null=True, blank=True)
    communication = models.TextField(_("Communication"), null=True, blank=True)
    Elevation = models.TextField(_("Elevation"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)
    class Meta:
        verbose_name = "AIRPORT, AIRDROME AND AIRSTRIPE"
        verbose_name_plural = "AIRPORTS, AIRDROMES AND AIRSTRIPES"

    def __unicode__(self):
        return self.location

EQUIPMENT_TYPE = (
    ("V", "Vehicle"),
    ("A", "Aircraft"),
    ("T", "Tractor"),
    ("O", "Other"),
)
class DisasterEquipment(models.Model):
    name = models.CharField(_("Equipment Name"), max_length=255, null=True, blank=True)
    number = models.CharField(_("Number of Equipments (How many)"), max_length=255, null=True, blank=255)
    description = models.TextField(_("Notes On Equipment"), null=True, blank=255)
    location = models.CharField(_("Location"), max_length=255, null=True, blank=True)
    longitude = models.CharField(_("Longitude"), max_length=255, null=True, blank=True)
    latitude = models.CharField(_("Latitude"), max_length=255, null=True, blank=True)
    _type = models.CharField(_("Equipment Type"), max_length=255, null=True, blank=True, choices=EQUIPMENT_TYPE)
    capacity = models.CharField(_("Equipment Capacity"), max_length=255, null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)
    class Meta:
        verbose_name = "DISASTER MANAGEMENT EQUIPMENT"
        verbose_name_plural = "DISASTER MANAGEMENT EQUIPMENTS"

    def __unicode__(self):
        return self.number

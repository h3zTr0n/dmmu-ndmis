# coding: UTF-8
# __author__: Alison Mukoma
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# from organization.models import Organization

class Ministry(models.Model):
    name = models.CharField(_("Ministry Name"), help_text=_("e.g  Home Affairs etc"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "MINISTRY"
        verbose_name_plural = "MINISTRIES"

    def __unicode__(Self):
        return self.name
#
# class CommitteeType(models.Model):
#         name = models.CharField(_("Ministry Type"), help_text=_("e.g  etc"), max_legnth=255)
#         created = models.DateTimeField(auto_now_add=True)
#         class Meta:
#             verbose_name = "COMMITTEE"
#             verbose_name_plural = "ZAMBIA VULNERABLITY ASSESSMENT COMMITTEES"
#
#         def __unicode__(Self):
#             return self.name

class TechnicalCommittee(models.Model):
    # Appointed by the vice-president
    name = models.CharField(_("Committee Name"), max_length=255,null=True, blank=True)
    ministry = models.ForeignKey(Ministry)
    # committee_type = models.ForeignKey(CommitteeType)
    national_cordinator = models.CharField(_("National Co-ordinator (Chairperson)"), max_length=255)
    permernent_secretary = models.CharField(_("Permanent Secretary Responsible for Defence (Vice-Chairperson)"), max_length=255)
    ps_national_planning = models.CharField(_("Permanent Secreary Responsible for National Planning"), max_length=255)
    ps_local_government = models.CharField(_("Permanent Secreary Responsible for Local Government"), max_length=255)
    ps_home_affairs = models.CharField(_("Permanent Secreary Responsible for Home Affairs"), max_length=255)
    ps_health = models.CharField(_("Permanent Secreary Responsible for Health"), max_length=255)
    ps_energy = models.CharField(_("Permanent Secreary Responsible for Energy"), max_length=255)
    ps_agriculture = models.CharField(_("Permanent Secreary Responsible for Agriculture"), max_length=255)
    ps_environment_and_natural_resources = models.CharField(_("Permanent Secreary Responsible for Environment and Natural Resources"), max_length=255)
    ps_communications = models.CharField(_("Permanent Secreary Responsible for Communications"), max_length=255)
    ps_minerals_development = models.CharField(_("Permanent Secreary Responsible for Minerals Development"), max_length=255)
    ps_information_and_broadcasting = models.CharField(_("Permanent Secreary Responsible for Information and Broadcasting"), max_length=255)
    ps_community_development= models.CharField(_("Permanent Secreary Responsible for Community Development"), max_length=255)
    ps_works_and_supply = models.CharField(_("Permanent Secreary Responsible for Works and Supply"), max_length=255)
    red_cross_society = models.CharField(_("Zambia Red Cross Society Representative"), max_length=255)
    un_resident_coordinator = models.CharField(_("United Nations Resident Coordinator"), max_length=255)
    religious_organization_representative = models.CharField(_("religious organisation Representative"), max_length=255)
    ex_officio_member = models.CharField(_("Ex Officio Member Approved by the VP"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "TECHNICAL COMMITTEE"
        verbose_name_plural = "TECHNICAL COMMITTEES"

    def __unicode__(self):
        return self.national_cordinator

class ProvincialCommittee(models.Model):
    # Definition of the nation disaster Technical Committee
    # part time members
    name = models.CharField(_("Province Name"), max_length=255,null=True, blank=True)
    provincial_ps = models.CharField(_("Provincial Permanent Secretary(Chairperson)"), max_length=255)
    gov_depts_repr_1 = models.CharField(_("Government Department Provincial Representative One"), max_length=255, null=True, blank=True)
    gov_depts_repr_2 = models.CharField(_("Government Department Provincial Representative Two"), max_length=255, null=True, blank=True)
    gov_depts_repr_3 = models.CharField(_("Government Department Provincial Representative Three"), max_length=255, null=True, blank=True)
    gov_depts_repr_4 = models.CharField(_("Government Department Provincial Representative Four"), max_length=255, null=True, blank=True)
    gov_depts_repr_5 = models.CharField(_("Government Department Provincial Representative Five"), max_length=255, null=True, blank=True)
    gov_depts_repr_6 = models.CharField(_("Government Department Provincial Representative Six"), max_length=255, null=True, blank=True)
    gov_depts_repr_7 = models.CharField(_("Government Department Provincial Representative Seven"), max_length=255, null=True, blank=True)
    pri_sector_repr_1 = models.CharField(_("Private Sector Representative One"), max_length=255, null=True, blank=True)
    pri_sector_repr_2 = models.CharField(_("Private Sector Representative Two"), max_length=255, null=True, blank=True)
    rel_org_repr_1 = models.CharField(_("Religious Organisation Representative One"), max_length=255, null=True, blank=True)
    rel_org_repr_2 = models.CharField(_("Religious Organisation Representative Two"), max_length=255, null=True, blank=True)
    pro_dis_mgnt_cord = models.CharField(_("Provincial Disaster Management CO-ordinator(Secretary)"), max_length=255, null=True, blank=True)
    vice_chairperson = models.CharField(_("Vice-Chairperson"), max_length=255, null=True, blank=True)
    co_ordinator = models.CharField(_("Co-ordinator(Public Officer)"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "PROVINCIAL COMMITTEE"
        verbose_name_plural = "PROVINCIAL COMMITTEES"

    def __unicode__(self):
        return self.provincial_ps

class DistrictCommittee(models.Model):
    name = models.CharField(_("District Name"), max_length=255,null=True, blank=True)
    co_ordinator = models.CharField(_("Co-ordinator(Chairperson)"), max_length=255, null=True, blank=True)
    gov_depts_repr_1 = models.CharField(_("Government Department District Representative One"), max_length=255, null=True, blank=True)
    gov_depts_repr_2 = models.CharField(_("Government Department District Representative Two"), max_length=255, null=True, blank=True)
    gov_depts_repr_3 = models.CharField(_("Government Department District Representative Three"), max_length=255, null=True, blank=True)
    gov_depts_repr_4 = models.CharField(_("Government Department District Representative Four"), max_length=255, null=True, blank=True)
    gov_depts_repr_5 = models.CharField(_("Government Department District Representative Five"), max_length=255, null=True, blank=True)
    gov_depts_repr_6 = models.CharField(_("Government Department District Representative Six"), max_length=255, null=True, blank=True)
    gov_depts_repr_7 = models.CharField(_("Government Department District Representative Seven"), max_length=255, null=True, blank=True)
    all_parliament_members = models.TextField(_("All Parliament Members in District"), null=True, blank=True)
    zam_red_cross_repr = models.CharField(_("Zambia Red Cross Representative"), max_length=255, null=True, blank=True)
    each_ngo_repr = models.TextField(_("Each NGO representative"), null=True, blank=True)
    rel_org_repr = models.CharField(_("Religious Organisation Representative"), max_length=255, null=True, blank=True)
    zam_chamb_com_repr = models.CharField(_("Zambia Chamber of Commerce Representative"), max_length=255, null=True, blank=True)
    secretary = models.CharField(_("Secretary"), max_length=255, null=True, blank=True)
    co_opted_member = models.TextField(_("Co-opted/Other Members"), null=True, blank=True)
    class Meta:
        verbose_name = "DISTRICT COMMITTEE"
        verbose_name_plural = "DISTRICT COMMITTEES"


    def __unicode__(self):
        return self.co_ordinator

class SateliteCommittee(models.Model):
    chairperson = models.CharField(_("Chairperson"), max_length=255, null=True, blank=True)
    vice_chairperson = models.CharField(_("Vice-Chairperson"), max_length=255, null=True, blank=True)
    less_than_10_part_time_members = models.TextField(_("Not more than Ten Part time Members"), null=True, blank=True)
    trad_auth_repr = models.CharField(_("Traditional Authority Representative in Area"), max_length=255, null=True, blank=True)
    atleast_3_disast_train_locals = models.TextField(_("Atleast 3 Disaster Hazard Trained Locals"), null=True, blank=True)
    commu_org = models.CharField(_("Community Based Organization Representative"), max_length=255, null=True, blank=True)
    local_commu_man_Repr_1 = models.CharField(_("Loca community Representative (Man)"), max_length=255, null=True, blank=True)
    local_commu_man_Repr_2 = models.CharField(_("Loca community Representative (Man)"), max_length=255, null=True, blank=True)
    local_commu_woman_Repr_1 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    local_commu_woman_Repr_2 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    youth_popu_repr = models.TextField(_("Youth Population Representative(Atleast 1)"), null=True, blank=True)
    businessman_farmer = models.CharField(_("Prominent Businessman or Farmer"), max_length=255, null=True, blank=True)
    local_ngo_repr = models.CharField(_("Local NGO Representative"), max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "SATELITE COMMITTEE"
        verbose_name_plural = "SATELITE COMMITTEES"

    def __unicode__(self):
        return self.chairperson

class Province(models.Model):
    name = models.CharField(_("Province Name"), max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "PROVINCE"
        verbose_name_plural = "PROVINCES"

    def __unicode__(self):
        return self.name

class ReliefMaizeDistribution(models.Model):
    province = models.CharField(max_length=255, default=_("Central"))
    district = models.CharField(_("DISTRICT"), max_length=255, null=True, blank=True)
    quantity = models.CharField(_("QUANTITY(MT)"), max_length=255, null=True, blank=True)
    requisition = models.CharField(_("REQUISTION #"), max_length=255, null=True, blank=True)
    requisition_date = models.DateField(_("REQUISTION DATE"), max_length=255, null=True, blank=True)
    delivery_order_num = models.CharField(_("DELIVERY ORDER #"), max_length=255, null=True, blank=True)
    access_point = models.CharField(_("ACCESS POINT"), max_length=255, null=True, blank=True)
    project_implemting_partner = models.CharField(_("PROJECT IMPLEMENTING PARTNER"), max_length=255, null=True, blank=True)
    mou_number = models.CharField(_("MOU NUMBER"), max_length=255, null=True, blank=True)
    mou_amount = models.CharField(_("MOU AMOUNT"), max_length=255, null=True, blank=True)
    first_50_percent = models.CharField(_("1st 50%"), max_length=255, null=True, blank=True)
    first_50_percent_chq_num = models.CharField(_("1st 50% CHQ #"), max_length=255, null=True, blank=True)
    second_50_percent = models.CharField(_("2st 50%"), max_length=255, null=True, blank=True)
    second_50_percent_chq_num = models.CharField(_("2st 50% CHQ #"), max_length=255, null=True, blank=True)
    balance = models.CharField(_("BALANCE"), max_length=255, null=True, blank=True)
    comments = models.TextField(_("COMMENTS"), max_length=255, null=True, blank=True)
    ward = models.CharField(_("WARD"), max_length=255, null=True, blank=True)
    longitude = models.CharField(_("LONGITUDE"), max_length=255, null=True, blank=True)
    latitude = models.CharField(_("LATITUDE"), max_length=255, null=True, blank=True)
    # start_year = models.DateField(_("START_YEAR"), auto_now_add=False)
    # end_year = models.DateField(_("END_YEAR"), auto_now_add=False)

    class Meta:
        verbose_name = u"RELIEF MAIZE DISTRIBUTION"
        verbose_name_plural = u"RELIEF MAIZE DISTRIBUTIONS"

    def __unicode__(self):
        return self.province



class ZambiaVulnerabilityAssessmentCommittee(models.Model):
    chairperson = models.CharField(_("Chairperson"), max_length=255, null=True, blank=True)
    Secretariat = models.CharField(_("Secretariat"), max_length=255, null=True, blank=True)
    less_than_10_part_time_members = models.TextField(_("Not more than Ten Part time Members"), null=True, blank=True)
    # trad_auth_repr = models.CharField(_("Traditional Authority Representative in Area"), max_length=255, null=True, blank=True)
    # atleast_3_disast_train_locals = models.TextField(_("Atleast 3 Disaster Hazard Trained Locals"), null=True, blank=True)
    # commu_org = models.CharField(_("Community Based Organization Representative"), max_length=255, null=True, blank=True)
    organizations_representatives = models.TextField(_("Various Organizational Board Representatives"), null=True, blank=True)

    # local_commu_man_Repr_2 = models.CharField(_("Loca community Representative (Man)"), max_length=255, null=True, blank=True)
    # local_commu_woman_Repr_1 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    # local_commu_woman_Repr_2 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    # youth_popu_repr = models.TextField(_("Youth Population Representative(Atleast 1)"), null=True, blank=True)
    # businessman_farmer = models.CharField(_("Prominent Businessman or Farmer"), max_length=255, null=True, blank=True)
    # local_ngo_repr = models.CharField(_("Local NGO Representative"), max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "ZAMBIA VULNERABLITY ASSESSMENT COMMITTEE"
        verbose_name_plural = "ZAMBIA VULNERABLITY ASSESSMENT COMMITTEES"

    def __unicode__(self):
        return self.chairperson



class NationalDisasterManagementConsultativeForum(models.Model):
    chairperson = models.CharField(_("Chairperson"), max_length=255, null=True, blank=True)
    Secretariat = models.CharField(_("Secretariat"), max_length=255, null=True, blank=True)
    less_than_10_part_time_members = models.TextField(_("Not more than Ten Part time Members"), null=True, blank=True)
    # trad_auth_repr = models.CharField(_("Traditional Authority Representative in Area"), max_length=255, null=True, blank=True)
    # atleast_3_disast_train_locals = models.TextField(_("Atleast 3 Disaster Hazard Trained Locals"), null=True, blank=True)
    # commu_org = models.CharField(_("Community Based Organization Representative"), max_length=255, null=True, blank=True)
    organizations_representatives = models.TextField(_("Various Organizational Board Representatives"), null=True, blank=True)

    # local_commu_man_Repr_2 = models.CharField(_("Loca community Representative (Man)"), max_length=255, null=True, blank=True)
    # local_commu_woman_Repr_1 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    # local_commu_woman_Repr_2 = models.CharField(_("Loca community Representative (Woman)"), max_length=255, null=True, blank=True)
    # youth_popu_repr = models.TextField(_("Youth Population Representative(Atleast 1)"), null=True, blank=True)
    # businessman_farmer = models.CharField(_("Prominent Businessman or Farmer"), max_length=255, null=True, blank=True)
    # local_ngo_repr = models.CharField(_("Local NGO Representative"), max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "NATIONAL DISASTER MANAGEMENT CONSULTATIVE FORUM"
        verbose_name_plural = "NATIONAL DISASTER MANAGEMENT CONSULTATIVE FORUMS"

    def __unicode__(self):
        return self.chairperson

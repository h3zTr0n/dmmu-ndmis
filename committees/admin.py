from __future__ import absolute_import

from django.contrib import admin


from import_export import resources
from import_export.admin import ImportExportMixin

from .models import (Ministry, TechnicalCommittee, ProvincialCommittee,
                    DistrictCommittee, SateliteCommittee, Province, ReliefMaizeDistribution,
                    ZambiaVulnerabilityAssessmentCommittee, NationalDisasterManagementConsultativeForum
                    )

class MinistryResource(resources.ModelResource):
    class Meta:
        model = Ministry

class MinistryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'created']
    search_fields = ['name', 'created',]
    list_filter = ('name', 'created',)
    resource_class = MinistryResource
admin.site.register(Ministry, MinistryAdmin)

class TechnicalCommitteeResource(resources.ModelResource):
    class Meta:
        model = TechnicalCommittee

class TechnicalCommitteeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name' , 'ministry', 'national_cordinator',
                    'permernent_secretary', 'red_cross_society',
                    'un_resident_coordinator', 'religious_organization_representative'
                    ]
    search_fields = ['name' , 'ministry',]
    list_filter = ('name' , 'ministry',)
    resource_class = TechnicalCommitteeResource
admin.site.register(TechnicalCommittee, TechnicalCommitteeAdmin)

class ProvincialCommitteeResource(resources.ModelResource):
    class Meta:
        model = ProvincialCommittee

class ProvincialCommitteeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'provincial_ps', 'pro_dis_mgnt_cord',
                    'vice_chairperson', 'co_ordinator'
                    ]

    search_fields = ['name', 'provincial_ps',
                    'pro_dis_mgnt_cord', 'vice_chairperson',]

    list_filter = ('name', 'provincial_ps', 'pro_dis_mgnt_cord',
                    'vice_chairperson',)
    resource_class = ProvincialCommitteeResource
admin.site.register(ProvincialCommittee, ProvincialCommitteeAdmin)

class DistrictCommitteeResource(resources.ModelResource):
    class Meta:
        model = DistrictCommittee

class DistrictCommitteeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'co_ordinator', 'zam_red_cross_repr',
                    'rel_org_repr', 'zam_chamb_com_repr', 'secretary'
                    ]
    search_fields = ['name', 'co_ordinator', 'zam_red_cross_repr',
                    'rel_org_repr', 'zam_chamb_com_repr',]

    list_filter = ('name', 'co_ordinator', 'zam_red_cross_repr',)
    resource_class = DistrictCommitteeResource
admin.site.register(DistrictCommittee, DistrictCommitteeAdmin)

class SateliteCommitteeResource(resources.ModelResource):
    class Meta:
        model= SateliteCommittee

class SateliteCommitteeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['chairperson', 'vice_chairperson',
                    'trad_auth_repr', 'commu_org',
                    'youth_popu_repr', 'businessman_farmer', 'local_ngo_repr'
                    ]
    search_fields = ['chairperson', 'vice_chairperson',
                    'trad_auth_repr', 'commu_org', 'youth_popu_repr',]

    list_filter = ('chairperson', 'vice_chairperson', 'trad_auth_repr',
                    'commu_org', 'youth_popu_repr',)
    resource_class = SateliteCommitteeResource
admin.site.register(SateliteCommittee, SateliteCommitteeAdmin)

class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province

class ProvinceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'created']
    search_fields = ['name', 'created',]
    list_filter = ('name', 'created',)
    resource_class = ProvinceResource
admin.site.register(Province, ProvinceAdmin)

class ReliefMaizeDistributionResource(resources.ModelResource):
    class Meta:
        model = ReliefMaizeDistribution

class ReliefMaizeDistributionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['province', 'district', 'quantity',
                    'requisition', 'requisition_date',
                    'delivery_order_num', 'access_point',
                    'project_implemting_partner', 'mou_number',
                    'mou_amount', 'first_50_percent', 'first_50_percent_chq_num',
                    'second_50_percent', 'second_50_percent_chq_num',
                    'balance', 'comments', 'ward', 'longitude', 'latitude']

    search_fields = ['province', 'district', 'quantity',
                    'requisition', 'requisition_date',
                    'delivery_order_num', 'access_point',
                    'project_implemting_partner', 'mou_number',
                    'mou_amount', 'first_50_percent', 'first_50_percent_chq_num',
                    'second_50_percent', 'second_50_percent_chq_num',

                    'balance', 'comments', 'ward',]
    list_filter = ('province', 'district', 'quantity',
                    'requisition', 'requisition_date',
                    'delivery_order_num', 'access_point',
                    'project_implemting_partner', 'mou_number',
                    'mou_amount', 'first_50_percent', 'first_50_percent_chq_num',
                    'second_50_percent', 'second_50_percent_chq_num',
                    'balance', 'comments', 'ward',)

    resource_class = ReliefMaizeDistributionResource
admin.site.register(ReliefMaizeDistribution, ReliefMaizeDistributionAdmin)

class ZambiaVulnerabilityAssessmentCommitteeResource(resources.ModelResource):
    class Meta:
        model = ZambiaVulnerabilityAssessmentCommittee

class ZambiaVulnerabilityAssessmentCommitteeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['chairperson', 'Secretariat',
                    'less_than_10_part_time_members',
                    'organizations_representatives']

    search_fields = ['chairperson', 'Secretariat',
                    'less_than_10_part_time_members',
                    'organizations_representatives',]

    list_filter = ('chairperson', 'Secretariat',
                    'less_than_10_part_time_members',
                    'organizations_representatives',)

    resource_class = ZambiaVulnerabilityAssessmentCommitteeResource
admin.site.register(ZambiaVulnerabilityAssessmentCommittee,
                    ZambiaVulnerabilityAssessmentCommitteeAdmin
                    )

class NationalDisasterManagementConsultativeForumResource(resources.ModelResource):
    class Meta:
        model = NationalDisasterManagementConsultativeForum

class NationalDisasterManagementConsultativeForumAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['chairperson', 'Secretariat']
    search_fields = ['chairperson', 'Secretariat',]
    list_filter = ('chairperson', 'Secretariat',)
    resource_class = NationalDisasterManagementConsultativeForumResource
admin.site.register(NationalDisasterManagementConsultativeForum,
                    NationalDisasterManagementConsultativeForumAdmin
                    )

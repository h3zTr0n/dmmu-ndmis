from __future__ import absolute_import

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin 
from .models import MaizeRequisition

class MaizeRequisitionResource(resources.ModelResource):
    class Meta:
        model = MaizeRequisition
        # fields = ('date', 'to', 'source',)


class MaizeRequisitionModelAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["date","to","source","req_num","destination","item_descr","qty","unit","stock_code","remarks","prepared_by","prepared_by_signature_status","approved_by","approved_by_signature_status","authorised_by","authorised_by_signature_status"]
    search_fields = ["date","to","source","req_num","destination","item_descr","qty","unit","stock_code","remarks","prepared_by","prepared_by_signature_status","approved_by","approved_by_signature_status","authorised_by","authorised_by_signature_status",]
    list_filter = ("date","to","source","req_num",)
    resource_class = MaizeRequisitionResource
admin.site.register(MaizeRequisition, MaizeRequisitionModelAdmin)

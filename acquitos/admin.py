from __future__ import absolute_import

from django.contrib import admin
from .models import MaizeRequisition

class MaizeRequisitionModelAdmin(admin.ModelAdmin):
    list_display = ["date","to","source","req_num","destination","item_descr","qty","unit","stock_code","remarks","prepared_by","prepared_by_signature_status","approved_by","approved_by_signature_status","authorised_by","authorised_by_signature_status"]
admin.site.register(MaizeRequisition, MaizeRequisitionModelAdmin)

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.

class MaizeRequisition(models.Model):
    """
        Table for storing information on Maize Requisitions.
    """
    date = models.DateField(_("Date Prepared"), default=timezone.now)
    to = models.CharField(_("To"), max_length=255)
    source = models.CharField(_("Source(Place)"), max_length=255)
    req_num = models.CharField(_("Requisition Number"), max_length=255)
    destination = models.CharField(_("Destination(Place)"), max_length=255)
    item_descr = models.CharField(_("Item Description"), max_length=355)
    qty = models.CharField(_("Quantity (Qty)"), max_length=255)
    unit = models.CharField(_("Unit"), max_length=255)
    stock_code = models.CharField(_("Stock Code"), max_length=255)
    remarks = models.TextField(_("Remarks"), null=True, blank=True)
    prepared_by = models.CharField(_("Prepared by: (name):"), max_length=255)
    prepared_by_signature_status = models.BooleanField(_("Prepared by: (signature(signed/pending))"), default=0)
    approved_by = models.CharField(_("Approved by: (name):"), max_length=255)
    approved_by_signature_status = models.BooleanField(_("Approved by: (signature(signed/pending))"), default=0)
    authorised_by = models.CharField(_("Authorised by: (name):"), max_length=255)
    authorised_by_signature_status = models.BooleanField(_("Authorised by: (signature(signed/pending))"), default=0)

    class Meta:
        verbose_name = "MAIZE REQUISITION"
        verbose_name_plural = "MAIZE REQUISITIONS"

    def __unicode__(self):
        return self.req_num

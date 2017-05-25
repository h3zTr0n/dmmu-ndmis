from __future__ import absolute_import
from controlcenter import Dashboard, widgets
from committees.models import ReliefMaizeDistribution

class ModelItemList(widgets.ItemList):
    model = ReliefMaizeDistribution
    list_display = ('pk', 'province', 'quantity', 'requisition', 'first_50_percent')

class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )

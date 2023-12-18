from django.contrib import admin
from vendorapp.models import Vendor,PurchaseOrder,HistoricalPerformance

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)

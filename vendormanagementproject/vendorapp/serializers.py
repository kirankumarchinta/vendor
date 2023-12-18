from  rest_framework.serializers import ModelSerializer
from vendorapp.models import Vendor,PurchaseOrder

class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
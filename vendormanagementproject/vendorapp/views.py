from django.shortcuts import render
from vendorapp.models import PurchaseOrder,Vendor
from vendorapp.serializers import PurchaseOrderSerializer,VendorSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class VendorListCreateApiView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

class PurchaseListCreateApiView(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'id'



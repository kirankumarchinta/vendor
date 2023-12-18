from django.db.models import Count, Avg
from django.utils import timezone
from vendorapp.models import Vendor,PurchaseOrder,HistoricalPerformance

def update_vendor_performance_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(status='completed')

    # On-Time Delivery Rate
    on_time_delivery_count = completed_pos.filter(delivery_date__lte=timezone.now()).count()
    vendor.on_time_delivery_rate = (on_time_delivery_count / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    # Quality Rating Average
    vendor.quality_rating_avg = completed_pos.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    # Average Response Time
    response_times = completed_pos.filter(acknowledgment_date__isnull=False).annotate(response_time=Count('acknowledgment_date') - ('issue_date')).aggregate(Avg('response_time'))['response_time__avg'] or 0
    vendor.average_response_time = response_times

    # Fulfilment Rate
    vendor.fulfillment_rate = completed_pos.filter(status='completed', issues__isnull=True).count() / completed_pos.count() * 100 if completed_pos.count() > 0 else 0

    vendor.save()

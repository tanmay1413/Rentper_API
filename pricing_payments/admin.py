from django.contrib import admin
from .models import RoomPricing, ExtraServiceCharge, PaymentMode
# Register your models here.
admin.site.register(RoomPricing)
admin.site.register(ExtraServiceCharge)
admin.site.register(PaymentMode)

from django.contrib import admin
from .models import * 



@admin.register(RoomPricing)
class RoomPricingAdmin(admin.ModelAdmin):
  list_display = ['room_type','price_per_day','extra_guest_threshold','extra_guest_per_price']
  list_filter = ['room_type__hotel__name'] 
  search_fields = ['room_type__room_type','room_type__hotel__name'] 
  
@admin.register(ExtraServiceCharge)
class ExtraPricingAdmin(admin.ModelAdmin):
  list_display = ['hotel','service','price']
  list_filter = ['hotel','service__name'] 
  search_fields = ['hotel','service__name'] 
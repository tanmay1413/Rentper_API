from django.contrib import admin
from .models import * 

@admin.register(HotelPolicy)
class PolicyAdmin(admin.ModelAdmin):
  list_display = ['hotel','pets_allowed','check_in_time','check_out_time']
  search_fields = ['hotel__name', 'pets_allowed']
  list_filter = ['pets_allowed']
  
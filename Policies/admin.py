from django.contrib import admin
from .models import Policies
# Register your models here.
class PoliciesAdmin(admin.ModelAdmin):
    list_display=('hotel_info', 'cancellation_policy', 'pets_allowed', 'pets_detail', 'check_in_time', 'check_out_time')
    
admin.site.register(Policies,PoliciesAdmin)
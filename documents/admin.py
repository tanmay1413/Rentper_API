from django.contrib import admin
from .models import * 


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
  list_display = ['hotel','gst_number','pan_card']
  search_fields = [ 'hotel__name','gst_number']
  list_filter = ['hotel']
from django.contrib import admin
from .models import LegalDocument
# Register your models here.
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display=('hotel', 'gst_number')
    list_filter=('hotel',)
admin.site.register(LegalDocument,LegalDocumentAdmin)
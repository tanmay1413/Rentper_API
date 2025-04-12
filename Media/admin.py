from django.contrib import admin
from .models import Media 
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'hotel', 'room_type')
    search_fields=('hotel','room')
    
admin.site.register(Media, MediaAdmin)
from django.contrib import admin
from .models import HotelMedia, RoomTypeMedia

@admin.register(HotelMedia)
class HotelMediaAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'preview_file', 'uploaded_at']
    readonly_fields = ['preview_file', 'uploaded_at']
    list_filter = ['hotel']
    
    def preview_file(self, obj):
        if obj.file:
            if obj.file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                return f'<img src="{obj.file.url}" width="100" height="60" />'
            elif obj.file.name.lower().endswith(('.mp4', '.webm')):
                return f'<video width="150" height="80" controls><source src="{obj.file.url}" type="video/mp4"></video>'
        return "No Preview Available"
    
    preview_file.allow_tags = True
    preview_file.short_description = "Preview"


@admin.register(RoomTypeMedia)
class RoomTypeMediaAdmin(admin.ModelAdmin):
    list_display = ['room_type', 'get_hotel', 'preview_file', 'uploaded_at']
    readonly_fields = ['preview_file', 'uploaded_at']
    list_filter = ['room_type__hotel', 'room_type']
    
    def get_hotel(self, obj):
        return obj.room_type.hotel
    
    def preview_file(self, obj):
        if obj.file:
            if obj.file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                return f'<img src="{obj.file.url}" width="100" height="60" />'
            elif obj.file.name.lower().endswith(('.mp4', '.webm')):
                return f'<video width="150" height="80" controls><source src="{obj.file.url}" type="video/mp4"></video>'
        return "No Preview Available"
    
    get_hotel.short_description = 'Hotel'
    preview_file.allow_tags = True
    preview_file.short_description = "Preview"

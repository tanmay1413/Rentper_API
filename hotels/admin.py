from django.contrib import admin
from .models import (
    BedConfiguration, Amenity, specialService, SafetyFeature,
    Hotel, Contact, Address, Room, HotelDetail
)

# Master tables
@admin.register(BedConfiguration)
class BedConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name', 'type']

@admin.register(specialService)
class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(SafetyFeature)
class SafetyFeatureAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Inline Models
class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

class HotelDetailInline(admin.StackedInline):
    model = HotelDetail
    extra = 0
    filter_horizontal = ['hotel_amenities', 'safety_features', 'special_services']

# Main models
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name','address__state','address__city','contact__phone_number','contact__owner_first_name','contact__owner_last_name','contact__email']
    list_filter = ['name']
    inlines = [ContactInline, AddressInline, HotelDetailInline]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_type', 'hotel', 'total_rooms', 'occupancy_limit']
    list_filter = ['hotel','occupancy_limit','room_type']
    search_fields = ['room_type', 'hotel__name']
    filter_horizontal = ['bed_configurations', 'room_amenities']

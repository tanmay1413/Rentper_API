from django.contrib import admin
from hotels.models import Hotel, Rooms_Type, Room_Details, Amenities
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Rooms_Type)
admin.site.register(Room_Details)
admin.site.register(Amenities)
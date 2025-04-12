from django.contrib import admin
from hotels.models import Hotel, Rooms_Type, Room_Details, Amenities

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('Hotel_ID', 'hotel_name', 'state', 'city','room_Type')
    list_filter=('state', 'city')
    
   
class RoomsTypeAdmin(admin.ModelAdmin):
    list_display = ('Room_ID', 'room_type_name', 'price_per_night')
    list_filter=('room_type_name', 'price_per_night')

class RoomDetailsAdmin(admin.ModelAdmin):
    list_display=('Detail_ID','hotel','room_type','price','available_Rooms')  
    list_filter=('hotel', 'room_type')
    search_fields=('hotel__hotel_name', 'room_type__room_type_name')

class AmentiesAdmin(admin.ModelAdmin):
    list_display=('Hotel_ID','Room_id','name','price')
    list_filter=('Hotel_ID', 'Room_id')
        

       
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Rooms_Type,RoomsTypeAdmin)
admin.site.register(Room_Details,RoomDetailsAdmin)
admin.site.register(Amenities,AmentiesAdmin)
from django.db import models

from hotels.models import Hotel , Room

# Create your models here.

class HotelMedia(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='gallery/hotel_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotel.name + " " + self.file.name


class RoomTypeMedia(models.Model):
    room_type = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='gallery/room_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room_type.room_type + " " + self.file.name

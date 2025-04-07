from django.db import models
from django.core.exceptions import ValidationError
import os
# from .models import Hotel, Rooms_Type, Room_Details, Amenities
from hotels.models import Hotel, Rooms_Type, Room_Details, Amenities
# Create your models here.
from django.db import models

class Media(models.Model):
    IMAGE_FORMAT_CHOICES = [
        (".jpg", "JPG"),
        (".jpeg", "JPEG"),
        (".png", "PNG"),
    ]

    VIDEO_FORMAT_CHOICES = [
        (".mp4", "MP4"),
        (".mov", "MOV"),
        (".avi", "AVI"),
    ]

    image_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room_Details, on_delete=models.CASCADE, blank=True, null=True)
    room_type = models.ForeignKey(Rooms_Type, on_delete=models.CASCADE, blank=True, null=True)
    room_image=models.FileField(upload_to='media/',null=True, blank=True)
    hotel_image=models.FileField(upload_to='media/',null=True, blank=True)

   
from django.db import models
from hotels.models import Hotel ,Room, HotelDetail, specialService
# Create your models here.
class RoomPricing(models.Model):
    room_type = models.OneToOneField(Room, on_delete=models.CASCADE)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    extra_guest_threshold = models.IntegerField()
    extra_guest_per_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room_type} - ₹{self.price_per_day}"

  

class ExtraServiceCharge(models.Model):
    hotel = models.ForeignKey(HotelDetail, on_delete=models.CASCADE, related_name='extra_service_charges')
    service = models.ForeignKey(specialService, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.hotel.hotel.name} - {self.service}"
  
class PaymentMode(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name='payment_modes')
    modes = models.JSONField(default=list)

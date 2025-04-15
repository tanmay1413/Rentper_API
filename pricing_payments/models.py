from django.db import models
from hotels.models import Room, specialService
# Create your models here.
class RoomPricing(models.Model):
  room_type = models.ForeignKey(Room, on_delete=models.CASCADE)
  price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
  extra_guest_threshold = models.IntegerField()
  extra_guest_per_price = models.DecimalField(max_digits=10, decimal_places=2)
  
class ExtraServiceCharge(models.Model):
  service = models.ForeignKey(specialService, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  
class PaymentMode(models.Model):
    mode = models.CharField(max_length=100) 

from django.db import models
from hotels.models import Hotel, Rooms_Type
# Create your models here.
class Pricing(models.Model):
 type=(
  ("Cash","Cash"),
  ("Credit Card","Credit Card"),
  ("Debit Card","Debit Card"),
  ("UPI","UPI"),
  ("Net Banking","Net Banking"),
  ("Wallets","Wallets"),
 )
 room_type=models.ForeignKey(Rooms_Type, on_delete=models.CASCADE, blank=True, null=True)
 price=models.FloatField(blank=True, null=True)
 tax=models.FloatField(blank=True, null=True)
 extra_charges=models.FloatField(blank=True, null=True)
 mode_of_payment=models.CharField(choices=type, max_length=50, blank=True)

 def __str__(self):
    return f"{self.room_type} - {self.price}"
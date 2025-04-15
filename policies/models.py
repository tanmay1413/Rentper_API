
from django.db import models
from hotels.models import Hotel
class HotelPolicy(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="HotelPolicies")
    detailed_hotel_info = models.TextField(max_length=3000)
    cancellation_policy = models.TextField(max_length=3000)
    pets_allowed = models.BooleanField(default=False)
    pet_policy = models.TextField(max_length=2000, blank=True, null=True)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

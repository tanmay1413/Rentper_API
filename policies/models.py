
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
    def __str__(self):
        return f"Policy for {self.hotel.name} - Check-in: {self.check_in_time}, Check-out: {self.check_out_time}"
    
class CancellationPolicy(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="CancellationPolicies")
    policy_type=models.CharField(max_length=100, choices=[('flexible', 'Flexible (Free cancellation up to 24h before check-in)'),
            ('standard', 'Standard (48h before check-in, partial refund)'),
            ('saver', 'Saver (Non-refundable)')], default='standard')
    cancellation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    refund_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.policy_type} Policy for {self.hotel.name}"


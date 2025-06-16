from django.db import models
from django.conf import settings
from hotels.models import *
from policies.models import *
from pricing_payments.models import *
from accounts.models import CustomUser
from datetime import timezone
from decimal import Decimal


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews') 
    hotel_rating = models.IntegerField(null=True, blank=True) 
    amentities_rating=models.IntegerField(null=True, blank=True)
    hygiene_rating=models.IntegerField(null=True, blank=True)
    communication_rating=models.IntegerField(null=True, blank=True)
    location_rating=models.IntegerField(null=True, blank=True)
    price_rating=models.IntegerField(null=True, blank=True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email} on {self.hotel.name}"
    


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishlists')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        unique_together = ('user','hotel')   
        
    def __str__(self):
        return f"{self.user.email} - {self.hotel.name}"   

class Booking(models.Model):
  user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
  hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
  room=models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings',default=None)
  check_in_date = models.DateField()
  check_out_date = models.DateField()
  guest_count=models.IntegerField(default=1, blank=True, null=True)
  special_request = models.TextField(blank=True, null=True,default=None)
  extra_amenities=models.ManyToManyField(ExtraServiceCharge, blank=True, related_name='bookings',default=None)
  special_services = models.ManyToManyField(specialService,blank=True, related_name='bookings',default=None)
  cancellation_policy= models.ForeignKey(CancellationPolicy, on_delete=models.CASCADE, related_name='bookings',blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

#   def cancel_booking(self):
#       if self.cancellation_policy:
#           days_before_checkin = (self.check_in_date - timezone.now().date()).days
#           if days_before_checkin >= self.cancellation_policy.free_cancellation_until:
#                 return "Full refund eligible"
#           return f"Cancellation fee: {self.cancellation_policy.cancellation_fee}"
#       return "No cancellation policy linked"

  
  def __str__(self):
        return f"Booking by {self.user.email} for {self.hotel.name} from {self.check_in_date} to {self.check_out_date}"


class BookingAmenity(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, related_name='booking_amenities')

    # class Meta:
    #     unique_together = ('booking', 'amenity')

    def __str__(self):
        return f"Amenity {self.amenity.name} for booking {self.booking.id}"
    
# class Payment(models.Model):
#         booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
#         amount = models.DecimalField(max_digits=10, decimal_places=2)
#         status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('completed', 'Completed'),('failed', 'Failed') ], default='pending')
#         created_at = models.DateTimeField(auto_now_add=True)
#         payment_method=models.CharField(max_length=50,choices=[('credit_card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Phonepay', 'Phonepay'),('Cash','Cash')],default=None)
        # def calculate_amount(self):
        #  booking_price = self.booking.total_price  # Assuming total_price is calculated in Booking model
        #  tax = booking_price * Decimal('0.10')  # Assuming 10% tax
        #  service_charge = Decimal('50.00')  # Fixed service charge
        #  total_amount = booking_price + tax + service_charge
        #  return total_amount

        # def save(self, *args, **kwargs):
       
        #   if not self.amount:
        #     self.amount = self.calculate_amount()
        # super().save(*args, **kwargs)

        # def __str__(self):
        #  return f"Payment for Booking {self.booking.id} - {self.status} - {self.amount}"



from decimal import Decimal
from django.db import models
from .models import Booking, RoomPricing

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=20,choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50,choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('phonepay', 'PhonePay'), ('cash', 'Cash')],default='cash' )

    def calculate_amount(self):
        room = self.booking.room
        pricing = RoomPricing.objects.filter(room_type=room).first()
        base_price = pricing.price_per_day if pricing else Decimal('0')
        amenities_price = sum(item.charge for item in self.booking.extra_amenities.all())
        tax = base_price * Decimal('0.10')
        return base_price + amenities_price + tax

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = self.calculate_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status} - ₹{self.amount}"       
        

class Guest(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=10, choices=[('Female','female'),('Male','Male'),('kid','Kid')], default='Male')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Guest {self.name} for Booking {self.booking.id}"


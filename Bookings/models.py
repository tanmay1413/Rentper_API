from django.db import models
from hotels.views import  Room
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Booking(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date=models.DateField()
    check_out_date=models.DateField()

    def __str__(self):
        return f"Booking for {self.room} from {self.check_in_date} to {self.check_out_date}"
    
    def date(self):
        today=timezone.now().date()
        if self.check_in_date < today:
            return ValidationError("Check-in date cannot be in the past.")
        if self.check_out_date<=self.check_in_date:
            return ValidationError("Check-out date must be after check-in date.")
    
    def save(self, *args, **kwargs):
        self.date()
        super().save(*args, **kwargs)
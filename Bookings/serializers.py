from rest_framework import serializers
from .models import Booking
from django.utils import timezone


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

    def validate(self, data):
        today = timezone.now().date()

        if data['check_in_date'] < today:
            raise serializers.ValidationError("Check-in date cannot be in the past.")
        
        if data['check_out_date'] <= data['check_in_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        
        return data    
        


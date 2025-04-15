from rest_framework import serializers
from .models import HotelPolicy

class HotelPolicySerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)

    class Meta:
        model = HotelPolicy
        fields = '__all__'

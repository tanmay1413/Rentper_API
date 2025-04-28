from rest_framework import serializers
from .models import *
from hotels.serializers import HotelSerializer, RoomSerializer, HotelDetailSerializer, SpecialServiceSerializer

class RoomPricingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), write_only=True
    )
    room_type_id = serializers.IntegerField(source='room_type.id', read_only=True)  # add this line

    class Meta:
        model = RoomPricing
        fields = [
            'id',
            'room',
            'room_id',           # for POST/PUT
            'room_type_id',      # for GET response
            'price_per_day',
            'extra_guest_threshold',
            'extra_guest_per_price'
        ]

    def create(self, validated_data):
        room = validated_data.pop('room_id')
        validated_data['room_type'] = room
        return RoomPricing.objects.create(**validated_data)

    def validate_room_id(self, value):
        if RoomPricing.objects.filter(room_type=value).exists():
            raise serializers.ValidationError("Pricing for this room already exists.")
        return value



class ExtraServiceChargeSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.hotel.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = ExtraServiceCharge
        fields = ['id', 'hotel', 'hotel_name', 'service', 'service_name', 'price']

    def validate(self, data):
        """
        Check if the service is already associated with the hotel.
        """
        hotel = data.get('hotel')
        service = data.get('service')

        # Check if this hotel-service combination already exists
        if ExtraServiceCharge.objects.filter(hotel=hotel, service=service).exists():
            raise serializers.ValidationError("This service is already associated with the hotel.")

        return data

    
class PaymentModeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PaymentMode
    fields = ['id', 'hotel', 'modes']
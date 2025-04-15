from rest_framework import serializers
from .models import *
from hotels.serializers import RoomSerializer, SpecialServiceSerializer


class RoomPricingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), write_only=True
    )

    class Meta:
        model = RoomPricing
        fields = [
            'id',
            'room',
            'room_id',
            'price_per_day',
            'extra_guest_threshold',
            'extra_guest_per_price'
        ]

    def create(self, validated_data):
        room_type = validated_data.pop('room_id')  # `room_id` already gives a Room instance
        validated_data['room_type'] = room_type
        return RoomPricing.objects.create(**validated_data)



class ExtraServiceChargeSerializer(serializers.ModelSerializer):
  service = SpecialServiceSerializer(read_only = True)
  service_id = serializers.PrimaryKeyRelatedField(
    queryset = specialService.objects.all(), write_only = True
  )
  class Meta:
    model = ExtraServiceCharge
    fields = ['id', 'service', 'service_id', 'price']
  
  def create(self, validated_data):
    service = validated_data.pop('service_id')
    return ExtraServiceCharge.objects.create(service=service, **validated_data)
  
    
class PaymentModeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PaymentMode
    fields = '__all__'
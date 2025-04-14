from rest_framework import serializers
from .models import HotelMedia, RoomTypeMedia

class HotelMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelMedia
        fields = ['id', 'hotel', 'file', 'uploaded_at']

class RoomTypeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypeMedia
        fields = ['id', 'room_type', 'file', 'uploaded_at']

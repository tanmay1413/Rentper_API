from hotels.models import Hotel, Room_Details,Rooms_Type,Amenities
from rest_framework import serializers

class HotelSerializer(serializers.ModelSerializer):
    class Meta :
        model=Hotel
        fields='__all__'

class RoomDetailsSerializer(serializers.ModelSerializer):
    class Meta :
        model=Room_Details
        fields='__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta :
        model=Rooms_Type
        fields='__all__'

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta :
        model= Amenities
        fields='__all__'

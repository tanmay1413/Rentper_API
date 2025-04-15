# from hotels.models import Hotel, Room_Details,Rooms_Type,Amenities
# from rest_framework import serializers

# class HotelSerializer(serializers.ModelSerializer):
#     class Meta :
#         model=Hotel
#         fields='__all__'

# class RoomDetailsSerializer(serializers.ModelSerializer):
#     class Meta :
#         model=Room_Details
#         fields='__all__'

# class RoomTypeSerializer(serializers.ModelSerializer):
#     class Meta :
#         model=Rooms_Type
#         fields='__all__'

# class AmenitiesSerializer(serializers.ModelSerializer):
#     class Meta :
#         model= Amenities
#         fields='__all__'


from rest_framework import serializers
from .models import *

class BedConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedConfiguration
        fields = ['id', 'name']

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'type']
        
class SpecialServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = specialService
        fields = ['id', 'name']

class SafetyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyFeature
        fields = ['id', 'name']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    bed_configurations = serializers.PrimaryKeyRelatedField(many=True, queryset=BedConfiguration.objects.all())
    room_amenities = serializers.PrimaryKeyRelatedField(many=True, queryset=Amenity.objects.filter(type='room'))

    class Meta:
        model = Room
        fields = '__all__'

class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_amenities = serializers.PrimaryKeyRelatedField(many=True, queryset=Amenity.objects.filter(type='hotel'))
    safety_features = serializers.PrimaryKeyRelatedField(many=True, queryset=SafetyFeature.objects.all())
    special_services = serializers.PrimaryKeyRelatedField(many=True, queryset=specialService.objects.all())

    class Meta:
        model = HotelDetail
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description']

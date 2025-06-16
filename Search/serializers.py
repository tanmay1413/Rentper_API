from rest_framework import serializers
from hotels.models import *
from policies.models import *
from Bookings.models import *
from gallery.models import *
from pricing_payments.models import *
from .models import *
from decimal import Decimal
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'city', 'state', 'zip_code', 'landmark']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['id','check_in_date','check_out_date','room']

class HotelMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelMedia
        fields =['file']

class RoomTypeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomTypeMedia
        fields=['file']                

class HotelSearchSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    bookings=serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    total_rooms = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'bookings', 'image', 'total_rooms']

    def get_address(self, obj):
        try:
            return AddressSerializer(obj.address).data
        except Address.DoesNotExist:
            return None
        
    def get_bookings(self, obj):
        
        check_in = self.context.get('check_in')
        check_out = self.context.get('check_out')
        bookings = Booking.objects.filter(room__hotel=obj)
        if check_in and check_out:
            bookings = bookings.filter(
                check_in__lt=check_out,
                check_out__gt=check_in)
        return BookingSerializer(bookings, many=True).data

    def get_image(self, obj):
        media = HotelMedia.objects.filter(hotel=obj).first()
        if media and media.file:
            request = self.context.get('request')
            return request.build_absolute_uri(media.file.url) if request else media.file.url
        return None

    def get_total_rooms(self, obj):
        return RoomTypeMedia.objects.filter(room_type__hotel=obj).count()


class TopRatedHotelSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    image = serializers.SerializerMethodField()
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'image', 'average_rating']

    def get_image(self, obj):
        media = HotelMedia.objects.filter(hotel=obj).first()
        if media:
            request = self.context.get('request')
            return request.build_absolute_uri(media.file.url) if request else media.file.url
        return None
                         # --------------hotel  detail --------------------- 

class HotelMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelMedia
        fields=['file']

class RoomMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomTypeMedia
        fields=['file']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['room_type','bathrooms','bedrooms','occupancy_limit','media']


class SafetyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
       model=SafetyFeature
       fields=['name']


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenity
        fields=['name']


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelPolicy
        fields=['check_in_time','check_out_time']

class SpecialServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=specialService
        fields=['name']
    


class HotelDetailSerializer(serializers.ModelSerializer): 
    address = AddressSerializer(read_only=True)
    image= serializers.SerializerMethodField()
    rooms = serializers.SerializerMethodField()
    policies = serializers.SerializerMethodField()
    safety = serializers.SerializerMethodField()
    amenities = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    review=serializers.SerializerMethodField()

    class Meta :
        model=Hotel
        fields=['id','name','address','image','rooms','policies','safety','amenities','services','review']
    
   
    def get_image(self, obj):
      media = HotelMedia.objects.filter(hotel=obj)
      return HotelMediaSerializer(media, many=True).data

    def get_rooms(self,obj):
        room=Room.objects.filter(hotel=obj)
        return RoomSerializer(room,many=True).data
    
    def get_policies(self,obj):
        policies=HotelPolicy.objects.filter(hotel=obj)
        return PolicySerializer(policies,many=True).data
    
    def get_amenities(self, obj):
        try:
            detail = obj.hoteldetail
            return AmenitySerializer(detail.hotel_amenities.all(), many=True).data
        except HotelDetail.DoesNotExist:
            return []

    def get_safety(self, obj):
        try:
            detail = obj.hoteldetail
            return SafetyFeatureSerializer(detail.safety_features.all(), many=True).data
        except HotelDetail.DoesNotExist:
            return []

    def get_services(self, obj):
        try:
            detail = obj.hoteldetail
            return SpecialServiceSerializer(detail.special_services.all(), many=True).data
        except HotelDetail.DoesNotExist:
            return []
        
    def get_review(self,obj):
        review=Review.objects.filter(hotel=obj)
        return ReviewSerializer(review,many=True).data    
    
  #------------------ room detail ---------------------
   
class RoomDetailSerializer(serializers.ModelSerializer):
    room_amenities = AmenitySerializer(many=True)
    bed_configurations = serializers.StringRelatedField(many=True)
    media = RoomMediaSerializer(many=True, read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True) 
  
    class Meta:
        model = Room
        fields = ['hotel','room_type', 'bathrooms', 'bedrooms', 'occupancy_limit', 'room_amenities', 'bed_configurations', 'media']
       

       #----------Review serializer------------

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review       
        fields=['hotel','user','hotel_rating','amentities_rating','hygiene_rating','communication_rating','location_rating','price_rating','review','created_at',]
   
    #-------wishlist serializer----
class WishlistSerializer(serializers.ModelSerializer):  
    hotel=HotelDetailSerializer(read_only=True)
    hotel_id = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(), source='hotel', write_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'hotel', 'hotel_id', 'created_at']
#   ----------Booking serializer----------------

class BookingAmenitySerializer(serializers.ModelSerializer):
    amenity_name = serializers.CharField(source="amenity.name", read_only=True)

    class Meta:
        model = BookingAmenity
        fields = ['amenity', 'amenity_name', 'charge']


class BookingSerializer(serializers.ModelSerializer):
    extra_amenities = BookingAmenitySerializer(many=True, write_only=True)
    special_services = serializers.PrimaryKeyRelatedField(queryset=specialService.objects.all(), many=True)
    total_price = serializers.SerializerMethodField()
    cancellation_policy = serializers.PrimaryKeyRelatedField(queryset=CancellationPolicy.objects.all(), write_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'hotel', 'room', 'check_in_date', 'check_out_date', 'guest_count',
            'special_request', 'special_services', 'extra_amenities', 'cancellation_policy', 'total_price']

    def get_total_price(self, obj):
        pricing = RoomPricing.objects.filter(room_type=obj.room).first()
        base_price = pricing.price_per_day if pricing else Decimal('0')
        amenities_price = sum(item.charge for item in obj.extra_amenities.all())
        taxes = base_price * Decimal('0.10')  # Convert tax rate to Decimal
        return base_price + amenities_price + taxes

    def create(self, validated_data):
        amenities_data = validated_data.pop('extra_amenities', [])
        special_services = validated_data.pop('special_services', [])
        cancellation_policy = validated_data.pop('cancellation_policy', None)
        user = self.context['request'].user

        booking = Booking.objects.create(user=user, cancellation_policy=cancellation_policy, **validated_data)
        booking.special_services.set(special_services)

        BookingAmenity.objects.bulk_create([
            BookingAmenity(booking=booking, **amenity_data) for amenity_data in amenities_data
        ])

        return booking
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# ---------Reservation------

class ReservationSerializer(serializers.ModelSerializer):
    hotel = HotelDetailSerializer(read_only=True)
    room = RoomDetailSerializer(read_only=True)
    class Meta:
        model=Booking
        feilds=['id', 'hotel', 'room', 'check_in_date', 'check_out_date', 'guest_count', 'special_request', 'special_services', 'extra_amenities']



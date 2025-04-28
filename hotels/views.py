
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = HotelDetail.objects.all()
    serializer_class = HotelDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

# Dropdown options

class BedConfigViewSet(viewsets.ModelViewSet):
    queryset = BedConfiguration.objects.all()
    serializer_class = BedConfigurationSerializer

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class SafetyFeatureViewSet(viewsets.ModelViewSet):
    queryset = SafetyFeature.objects.all()
    serializer_class = SafetyFeatureSerializer

class SpecialServiceViewSet(viewsets.ModelViewSet):
    queryset = specialService.objects.all()
    serializer_class = SpecialServiceSerializer


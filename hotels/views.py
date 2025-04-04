from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from hotels.serializers import HotelSerializer, RoomDetailsSerializer, RoomTypeSerializer, AmenitiesSerializer
from hotels.models import Hotel, Room_Details, Rooms_Type, Amenities


# Create your views here.
class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

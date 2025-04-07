from django.shortcuts import render
from .models import Media
from .serializers import MediaSerializers
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
# class MediaList(generics.ListCreateAPIView):
#     queryset = Media.objects.all()
#     serializer_class = MediaSerializers

#     def get_queryset(self):
#         hotel_id=self.kwargs['hotel_id']
#         return Media.objects.filter(hotel_id=hotel_id)

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         look_field = 'hotel_id' 
#         if serializer.is_valid():
#             serializer.save(hotel_id=self.kwargs['hotel_id'])
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HotelImageList(generics.ListCreateAPIView):
    serializer_class=MediaSerializers

    def get_queryset(self):
         hotel_id=self.kwargs['hotel_id']
         return Media.objects.filter(hotel_id=hotel_id).exclude(hotel_image=None)

    def perform_create(self, serializer):
         hotel_id=self.kwargs['hotel_id']
         serializer.save(hotel_id=hotel_id)     

class HotelImageView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Media.objects.exclude(hotel_image=None)
     serializer_class=MediaSerializers
     lookup_field = 'image_id' # This is the field used to look up the hotel instance.   
        
        

class RoomList(generics.ListCreateAPIView):
    serializer_class=MediaSerializers

    def get_queryset(self):
         room_id=self.kwargs['room_id']
         return Media.objects.filter(room_id=room_id).exclude(room_image=None)
    
    def perform_create(self, serializer):
         room_id=self.kwargs['room_id']
         serializer.save(room_id=room_id)

class RoomImageView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Media.objects.exclude(room_image=None)         
     serializer_class=MediaSerializers
     lookup_field='image_id'
# from django.shortcuts import render
# from datetime import datetime

# from rest_framework import viewsets,generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import authentication, permissions,status
# from rest_framework.decorators import api_view, permission_classes
# from hotels.serializers import HotelSerializer, RoomDetailsSerializer, RoomTypeSerializer, AmenitiesSerializer
# from hotels.models import Hotel, Room_Details, Rooms_Type, Amenities


# # Create your views here.
# class HotelList(generics.ListCreateAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()  # Saves the hotel without checking user roles
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# # class HotelList(generics.ListCreateAPIView):
# #     queryset = Hotel.objects.all()
# #     serializer_class = HotelSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     # def perform_create(self, serializer):
#     #       if self.request.user.role != 'hotel_owner':
#     #         return Response({'error': 'Only hotel owners can add hotels'}, status=status.HTTP_403_FORBIDDEN)
#     #       serializer.save(owner=self.request.user)
#        # role field required to save the data 

# # This view handles the retrieval, update, and deletion of a hotel instance.
# class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
#      queryset=Hotel.objects.all()
#      serializer_class=HotelSerializer
#     #  permission_classes=[permissions.IsAuthenticated]
#      lookup_field = 'Hotel_ID' # This is the field used to look up the hotel instance.

     
         
# class RoomDetailsList(generics.ListCreateAPIView):
#     queryset = Room_Details.objects.all()
#     serializer_class = RoomDetailsSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     def get_queryset(self):
#         hotel_id=self.kwargs['hotel_id']
#         return Room_Details.objects.filter(hotel_id=hotel_id)
       
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         look_field = 'hotel_id' 
#         if serializer.is_valid():
#             serializer.save(hotel_id=self.kwargs['hotel_id'])
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
# class RoomDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room_Details.objects.all()
#     serializer_class = RoomDetailsSerializer
#     lookup_field = 'Detail_ID'   
    

# # class RoomDetailsList(generics.ListCreateAPIView):
# #     serializer_class = RoomDetailsSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def get_queryset(self):
# #         hotel_id = self.kwargs['hotel_id']
# #         return Room_Details.objects.filter(hotel_id=hotel_id)

# #     def perform_create(self, serializer):
# #         serializer.save(hotel_id=self.kwargs['hotel_id'])

# #     def list(self, request, *args, **kwargs):
# #         queryset = self.get_queryset()
# #         serializer = self.get_serializer(queryset, many=True)

# #         today = datetime.today().weekday()  # 0=Monday, 6=Sunday

# #         updated_data = []
# #         for item in serializer.data:
# #             base_price = item.get('Price', 0)
# #             try:
# #                 base_price = float(base_price)
# #             except:
# #                 base_price = 0

# #             # Apply weekend pricing (just added a simple example)
# #             final_price = base_price * 1.2 if today in [5, 6] else base_price
# #             item_with_price = dict(item)
# #             item_with_price['final_price'] = round(final_price, 2)
# #             updated_data.append(item_with_price)

# #         return Response(updated_data, status=status.HTTP_200_OK)


# class RoomTypeList(generics.ListCreateAPIView):
#     queryset = Rooms_Type.objects.all()
#     serializer_class = RoomTypeSerializer
#     # permission_classes = [permissions.IsAuthenticated]

# class AmenitiesList(generics.ListCreateAPIView):
#     queryset=Amenities.objects.all()
#     serializer_class=AmenitiesSerializer
#     # permission_classes=[permissions.IsAuthenticated]
       
# class AmenitiesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Amenities.objects.all()
#     serializer_class=AmenitiesSerializer
#     lookup_field='Hotel_ID'


from rest_framework import viewsets
from .models import *
from .serializers import *

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = HotelDetail.objects.all()
    serializer_class = HotelDetailSerializer

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


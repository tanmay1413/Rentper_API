from django.urls import path
from .views import HotelList,HotelDetailView,RoomDetailsList,RoomTypeList,AmenitiesList,RoomDetailsDetailView,AmenitiesDetailView


urlpatterns = [
 path('hotels/', HotelList.as_view(), name='hotel-list'),  #create a hotel details
 path('hotels/<int:Hotel_ID>/', HotelDetailView.as_view(), name='hotel-detail'), #retrieve, update and delete a hotel details
path('hotels/<int:hotel_id>/rooms/', RoomDetailsList.as_view(), name='room-list'),  #list and create a room details
path('rooms/<int:Detail_ID>/', RoomDetailsDetailView.as_view(), name='room-detail'), #retrieve, update and delete a room details
path('roomtype/', RoomTypeList.as_view(), name='room-type-list'),  #list all room types
path('amenities/', AmenitiesList.as_view(), name='amenities-list'), #list all amenities
path('amenities/<int:Hotel_ID>/', AmenitiesDetailView.as_view(), name='amenities-detail'), #retrieve, update and delete a amenities details
]
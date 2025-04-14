# from django.urls import path
# from .views import HotelList,HotelDetailView,RoomDetailsList,RoomTypeList,AmenitiesList,RoomDetailsDetailView,AmenitiesDetailView


# urlpatterns = [
#  path('api/hotel/', HotelList.as_view(), name='hotel-list'),  #create a hotel details
#  path('hotels/<int:Hotel_ID>/', HotelDetailView.as_view(), name='hotel-detail'), #retrieve, update and delete a hotel details
# path('hotels/<int:hotel_id>/rooms/', RoomDetailsList.as_view(), name='room-list'),  #list and create a room details
# path('rooms/<int:Detail_ID>/', RoomDetailsDetailView.as_view(), name='room-detail'), #retrieve, update and delete a room details
# path('roomtype/', RoomTypeList.as_view(), name='room-type-list'),  #list all room types
# path('amenities/', AmenitiesList.as_view(), name='amenities-list'), #list all amenities
# path('amenities/<int:Hotel_ID>/', AmenitiesDetailView.as_view(), name='amenities-detail'), #retrieve, update and delete a amenities details
# ]


from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('contacts', ContactViewSet)
router.register('addresses', AddressViewSet)
router.register('rooms', RoomViewSet)
router.register('details', HotelDetailViewSet)

# Dropdowns
router.register('bed-configs', BedConfigViewSet)
router.register('amenities', AmenityViewSet)
router.register('special-service',SpecialServiceViewSet)
router.register('safety-features', SafetyFeatureViewSet)

urlpatterns = router.urls

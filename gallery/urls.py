from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelMediaViewSet, RoomTypeMediaViewSet

router = DefaultRouter()
router.register(r'hotel-media', HotelMediaViewSet, basename='hotel-media')
router.register(r'room-type-media', RoomTypeMediaViewSet, basename='room-type-media')

urlpatterns = [
    path('', include(router.urls)),
]

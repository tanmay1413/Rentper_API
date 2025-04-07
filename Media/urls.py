from django.urls import path
from .views import HotelImageList,HotelImageView,RoomList,RoomImageView

urlpatterns = [
    path('hotels/<int:hotel_id>/images/', HotelImageList.as_view(), name='hotel-image-list'), 
    path('hotels/images/<int:image_id>/', HotelImageView.as_view(), name='hotel-image-detail'),  #retrieve, update and delete a hotel image
    path('rooms/<int:room_id>/images/', RoomList.as_view(), name='room-image-list'),
    path('rooms/images/<int:image_id>/', RoomImageView.as_view(), name='room-image-detail'),  #retrieve update and delete a room image 
    
]

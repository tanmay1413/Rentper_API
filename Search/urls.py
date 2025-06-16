# urls.py
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register(r'wishlist', WishlistView, basename='wishlist')

urlpatterns = [
    # path('', include(router.urls)),  
    path('search/', HotelSearchAPIView.as_view(), name='hotel-search'),  # we will get hotel list based on search query
    path('top-rated/', TopRatedHotelsView.as_view(), name='top-rated-hotels'),  #  will get  top-rated hotel list
    path('hotel/<int:id>/', HotelDetail.as_view(), name='hotel-detail'), # will get hotel detail based on id
    path('room/', RoomDetailView.as_view(), name='room-detail'), # will get room list based on room-type
    path('review/', ReviewView.as_view({'get': 'list', 'post': 'create','delete':'destroy'}), name='review-list-create'), # will get review list and create review
    path('wishlist/', WishlistView.as_view(), name='wishlist-list-create'), # will get wishlist and create wishlist
    path('wishlist/<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'), # will delete wishlist based on id
    path('nearby/', NearbyHotelsView.as_view(), name='nearby-hotels'), # will get nearby hotels based on latitude and longitude
    path('booking/', BookingView.as_view(), name='booking-list-create'),  # will get booking list and create booking
    path('payment/', PaymentView.as_view(), name='payment-list-create'),  # will get payment list and create payment
    path('reservation/', ReservationView.as_view())
    ]

from django.urls import path
from .views import HotelListCreateView


urlpatterns = [
 path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
]
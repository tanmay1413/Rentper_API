from django.urls import path
from .views import bookings_chart
urlpatterns = [
    path('api/bookings-chart/', bookings_chart),
]

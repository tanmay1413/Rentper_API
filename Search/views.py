from rest_framework import viewsets, filters,generics, status
from rest_framework.filters import  SearchFilter
from hotels.models import *
from .serializers import *
from .filters import HotelFilter,RoomFilter
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from django.db.models import F, Avg
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated
from math import radians, cos, sin, asin, sqrt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class HotelSearchAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSearchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = HotelFilter
    search_fields = ['name', 'address__city']
    permission_classes = [AllowAny]

class TopRatedHotelsView(generics.ListAPIView):
    serializer_class = TopRatedHotelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Hotel.objects.annotate(
            average_rating=Avg(
                (F('reviews__hotel_rating') +
                 F('reviews__amentities_rating') +
                 F('reviews__hygiene_rating') +
                 F('reviews__communication_rating') +
                 F('reviews__location_rating') +
                 F('reviews__price_rating')) / 6.0 ) ).order_by('-average_rating')[:10]

class HotelDetail(generics.RetrieveAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelDetailSerializer  
    lookup_field='id'
    permission_classes = [AllowAny]


class RoomDetailView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomDetailSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=RoomFilter
    permission_classes = [AllowAny]


class ReviewView(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes = [AllowAny]

class WishlistView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishlistDeleteView(generics.DestroyAPIView):
    serializer_class = WishlistSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Wishlist.objects.filter(user=user)

# class WishlistView(viewsets.ModelViewSet):
#     serializer_class = WishlistSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Wishlist.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class NearbyHotelsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            lat, lon = float(request.query_params['latitude']), float(request.query_params['longitude'])
            radius = float(request.query_params.get('radius', 15))
        except (KeyError, ValueError):
            return Response({"error": "Valid latitude and longitude are required."}, status=400)

        def haversine(lon1, lat1, lon2, lat2):
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
            return 6371 * 2 * asin(sqrt(sin((lat2 - lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2 - lon1)/2)**2))

        hotels = [hotel for hotel in Hotel.objects.select_related('address')
            if hasattr(hotel, 'address') and hotel.address.latitude and hotel.address.longitude
            and haversine(lon, lat, hotel.address.longitude, hotel.address.latitude) <= radius]
        serializer = HotelDetailSerializer(hotels, many=True, context={'request': request})
        return Response(serializer.data)
    
class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Booking.objects.all()
 
class PaymentView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Payment.objects.filter(booking__user=self.request.user)
    def perform_create(self, serializer):
        serializer.save()


class ReservationView(generics.ListAPIView):
    serializer_class = BookingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






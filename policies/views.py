from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import HotelPolicy
from .serializers import HotelPolicySerializer

class HotelPolicyViewSet(ModelViewSet):
    queryset = HotelPolicy.objects.all()
    serializer_class = HotelPolicySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']
 
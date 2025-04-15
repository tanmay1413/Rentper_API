from rest_framework.viewsets import ModelViewSet
from .models import HotelPolicy
from .serializers import HotelPolicySerializer

class HotelPolicyViewSet(ModelViewSet):
    queryset = HotelPolicy.objects.all()
    serializer_class = HotelPolicySerializer

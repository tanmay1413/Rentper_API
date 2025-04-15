from rest_framework import viewsets
from .models import RoomPricing, ExtraServiceCharge, PaymentMode
from .serializers import (
    RoomPricingSerializer,
    ExtraServiceChargeSerializer,
    PaymentModeSerializer,
)

# Room pricing
class RoomPricingViewSet(viewsets.ModelViewSet):
    queryset = RoomPricing.objects.all()
    serializer_class = RoomPricingSerializer

# Extra service charge (linked to ExtraService model in hotels app)
class ExtraServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = ExtraServiceCharge.objects.all()
    serializer_class = ExtraServiceChargeSerializer

# Payment mode
class PaymentModeViewSet(viewsets.ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer


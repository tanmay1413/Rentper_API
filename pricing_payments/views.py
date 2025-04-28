from rest_framework import viewsets , status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import RoomPricing, ExtraServiceCharge, PaymentMode, HotelDetail
from .serializers import (
    RoomPricingSerializer,
    ExtraServiceChargeSerializer,
    PaymentModeSerializer,
)

# Room pricing
class RoomPricingViewSet(viewsets.ModelViewSet):
    queryset = RoomPricing.objects.all()
    serializer_class = RoomPricingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type__hotel']



# Payment mode
class PaymentModeViewSet(viewsets.ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer


class ExtraServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = ExtraServiceCharge.objects.all()
    serializer_class = ExtraServiceChargeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # Bulk create, validate each item in the list
            serializer = self.get_serializer(data=request.data, many=True)
            if serializer.is_valid(raise_exception=True):
                self.perform_bulk_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Single object create
            return super().create(request, *args, **kwargs)

    def perform_bulk_create(self, serializer):
        # Save each item after validation
        serializer.save()
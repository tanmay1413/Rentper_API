from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoomPricingViewSet,
    ExtraServiceChargeViewSet,
    PaymentModeViewSet,
)

router = DefaultRouter()
router.register(r'room-pricing', RoomPricingViewSet)
router.register(r'extra-service-charges', ExtraServiceChargeViewSet)
router.register(r'payment-modes', PaymentModeViewSet)

urlpatterns = router.urls
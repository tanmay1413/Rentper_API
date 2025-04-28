
from rest_framework.routers import DefaultRouter
from .views import HotelPolicyViewSet

router = DefaultRouter()
router.register(r'hotel-policies', HotelPolicyViewSet)

urlpatterns = router.urls

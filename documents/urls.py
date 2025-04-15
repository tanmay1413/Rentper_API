# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LegalDocumentViewSet

router = DefaultRouter()
router.register('legal-documents', LegalDocumentViewSet)

urlpatterns = router.urls
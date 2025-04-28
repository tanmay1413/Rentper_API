
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import LegalDocument
from .serializers import LegalDocumentSerializer

class LegalDocumentViewSet(viewsets.ModelViewSet):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

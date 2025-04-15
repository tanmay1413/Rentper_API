
from rest_framework import viewsets
from .models import LegalDocument
from .serializers import LegalDocumentSerializer

class LegalDocumentViewSet(viewsets.ModelViewSet):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer

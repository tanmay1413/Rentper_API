from rest_framework import generics, status
from rest_framework.response import Response
from .models import LegalDocument
from .serializers import LegalDocumentSerializer

# List all legal documents or create a new one with hotel_id in URL
class LegalDocumentList(generics.ListCreateAPIView):
    serializer_class = LegalDocumentSerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        return LegalDocument.objects.filter(hotel_id=hotel_id)

    def post(self, request, *args, **kwargs):
        hotel_id = self.kwargs.get('hotel_id')
        data = request.data.copy()
        data['hotel'] = hotel_id
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, delete a single legal document by its primary key (id)
class LegalDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer
    lookup_field = 'pk'  # You can use 'id' too if your URL pattern reflects that

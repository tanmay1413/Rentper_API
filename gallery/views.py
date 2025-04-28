from rest_framework.response import Response
from rest_framework import viewsets , status
from django_filters.rest_framework import DjangoFilterBackend
from .models import HotelMedia, RoomTypeMedia
from .serializers import HotelMediaSerializer, RoomTypeMediaSerializer


class HotelMediaViewSet(viewsets.ModelViewSet):
    queryset = HotelMedia.objects.all()
    serializer_class = HotelMediaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_id']

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        hotel_id = request.data.get('hotel')

        if not files:
            return Response({"error": "No files uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        media_instances = []
        for f in files:
            media_instances.append(HotelMedia(hotel_id=hotel_id, file=f))

        HotelMedia.objects.bulk_create(media_instances)
        return Response({"message": "Files uploaded successfully."}, status=status.HTTP_201_CREATED)

class RoomTypeMediaViewSet(viewsets.ModelViewSet):
    queryset = RoomTypeMedia.objects.all()
    serializer_class = RoomTypeMediaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type__hotel']

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        room_type_id = request.data.get('room_type')

        if not files:
            return Response({"error": "No files uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        media_instances = []
        for f in files:
            media_instances.append(RoomTypeMedia(room_type_id = room_type_id, file=f))

        RoomTypeMedia.objects.bulk_create(media_instances)
        return Response({"message": "Files uploaded successfully."}, status=status.HTTP_201_CREATED)

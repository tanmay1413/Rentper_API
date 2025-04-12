from django.shortcuts import render
from rest_framework import viewsets,generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from .models import Policies
from .serializers import PoliciesSerializer
# Create your views here.


class PoliciesList(generics.ListCreateAPIView):
    queryset=Policies.objects.all()
    serializer_class=PoliciesSerializer

    def get_queryset(self):
        hotel_info = self.kwargs.get('hotel_info')
        return Policies.objects.filter(hotel_info=hotel_info)

    def perform_create(self, serializer):
        hotel_info = self.kwargs.get('hotel_info')
        serializer.save(hotel_info=hotel_info)


class PoliciesCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset=Policies.objects.all()
    serializer_class=PoliciesSerializer
    lookup_field='pk'  # This is the field used to look up the hotel instance.    
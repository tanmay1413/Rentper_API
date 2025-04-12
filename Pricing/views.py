from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions,status
from rest_framework.decorators import api_view, permission_classes
from .models import Pricing
from .serializers import PricingSerializer
# Create your views here.

class PricingList(generics.ListCreateAPIView):
    queryset=Pricing.objects.all()
    serializer_class=PricingSerializer


class PricingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Pricing.objects.all()
    serializer_class=PricingSerializer
    lookup_field='room_type'
    



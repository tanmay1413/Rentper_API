from django.urls import path
from .views import PricingList

urlpatterns=[
    path('pricing/', PricingList.as_view(), name='pricing-list'),
]
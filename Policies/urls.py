from django.urls import path
from .views import PoliciesList,PoliciesCrud

urlpatterns = [
    path('policies/',PoliciesList.as_view(),name='policies-list'),
    path('policies/<int:pk>/',PoliciesCrud.as_view(),name='policies-detail')
]

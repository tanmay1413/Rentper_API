from django.urls import path
from .views import LegalDocumentList, LegalDocumentDetailView

urlpatterns = [
    path('hotel/<int:hotel_id>/documents/', LegalDocumentList.as_view(), name='legal-docs-list-create'),
    path('documents/<int:pk>/', LegalDocumentDetailView.as_view(), name='legal-doc-detail')
]

# documents/models.py

from django.db import models
from hotels.models import Hotel  

class LegalDocument(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name="legal_documents")
    gst_number = models.CharField(max_length=100)

    pan_card = models.FileField(upload_to='documents/pan_cards/', null=True, blank=True)
    hotel_license = models.FileField(upload_to='documents/hotel_licenses/', null=True, blank=True)
    hotel_ownership_proof = models.FileField(upload_to='documents/ownership_proofs/', null=True, blank=True)
    fssai_license = models.FileField(upload_to='documents/fssai_licenses/', null=True, blank=True)
    fire_safety_certificate = models.FileField(upload_to='documents/fire_safety_certificates/', null=True, blank=True)
    owner_identity_proof = models.FileField(upload_to='documents/owner_ids/', null=True, blank=True)
    manager_identity_proof = models.FileField(upload_to='documents/manager_ids/', null=True, blank=True)
    authorization_letter = models.FileField(upload_to='documents/authorization_letters/', null=True, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Legal Docs for {self.hotel.name}"

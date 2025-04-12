from django.db import models
from hotels.models import Hotel
# Create your models here.
class LegalDocument(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='legal_documents')
    gst_number=models.CharField(max_length=20, blank=True, null=True)
    pan_card=models.FileField(upload_to='legal_documents/pan_card/', blank=True, null=True)
    hotel_license=models.FileField(upload_to='legal_documents/hotel_license/', blank=True, null=True)
    ownership_proof=models.FileField(upload_to='legal_documents/ownership_proof/', blank=True, null=True)
    fssai_license=models.FileField(upload_to='legal_documents/fssai_license/', blank=True, null=True)
    fire_safety=models.FileField(upload_to='legal_documents/fire_safety/', blank=True, null=True)
    identity_proof=models.FileField(upload_to='legal_documents/identity_proof/', blank=True, null=True)
    managers_proof=models.FileField(upload_to='legal_documents/managers_proof/', blank=True, null=True)
    authorization_letter=models.FileField(upload_to='legal_documents/authorization_letter/', blank=True, null=True)

    def __str__(self):
        return f"Legal Document for {self.hotel.name}"
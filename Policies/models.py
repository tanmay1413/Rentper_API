from django.db import models
from datetime import time
# from hotels.models import Hotels
# Create your models here.
class Policies(models.Model):
    hotel_info=models.CharField(max_length=500,blank=True)
    cancellation_policy=models.CharField(max_length=500,blank=True,null=True)
    pets_allowed=models.CharField(max_length=10,choices=[("Yes","Yes"),("No","No")],blank=True,null=True)
    pets_detail=models.CharField(max_length=500,blank=True,null=True)
    check_in_time=models.TimeField(default=time(9, 0),blank=True,null=True)
    check_out_time=models.TimeField(default=time(9, 0),blank=True,null=True)

    
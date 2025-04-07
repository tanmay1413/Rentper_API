from django.contrib.auth.models import AbstractUser
from django.db import models

from Account.managers import CustomManager

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("vendor", "Vendor"),
        ("user", "User"),
    ]

    username = None
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=200, blank=True, choices=ROLE_CHOICES, default='user')
    profile_photo = models.ImageField(upload_to="Profile", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomManager()
    
    def __str__(self):
        return self.email
    

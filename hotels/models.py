

from django.db import models

# Master Tables
class BedConfiguration(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=[('room', 'Room'), ('hotel', 'Hotel')],
    )

    def __str__(self):
        return f"{self.name} ({self.type})"
    
class specialService(models.Model):
    name = models.CharField(max_length=50)
    # price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class SafetyFeature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Main Models
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Contact(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.owner_first_name + " " + self.owner_last_name

class Address(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    landmark = models.CharField(max_length=255)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    total_rooms = models.IntegerField()
    occupancy_limit = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    bed_configurations = models.ManyToManyField(BedConfiguration)
    room_amenities = models.ManyToManyField(Amenity, limit_choices_to={'type': 'room'})
    more = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}-{self.room_type} - {self.hotel.name}"

class HotelDetail(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    hotel_amenities = models.ManyToManyField(Amenity, limit_choices_to={'type': 'hotel'})
    safety_features = models.ManyToManyField(SafetyFeature)
    special_services = models.ManyToManyField(specialService,blank=True)
    more = models.TextField(blank=True, null=True)

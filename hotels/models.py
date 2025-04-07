from django.db import models

class Hotel(models.Model):
    Hotel_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    room_Type = models.ForeignKey('Rooms_Type', on_delete=models.CASCADE, blank=True, null=True)
    total_no_of_rooms = models.IntegerField(blank=True, null=True)
    safety_features = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True)
    nearby_mark = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name  

class Rooms_Type(models.Model):
    TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Quad', 'Quad'),
        ('Queen', 'Queen'),
        ('King', 'King'),
        ('Twin', 'Twin'),
        ('Suite', 'Suite')
    ]

    Room_ID = models.AutoField(primary_key=True)
    room_type_name = models.CharField(max_length=200, blank=True, choices=TYPES)  
    description = models.CharField(max_length=250, blank=True)    
    occupancy_limit = models.IntegerField(blank=True, null=True)
    types_of_bed = models.CharField(max_length=200, choices=TYPES, blank=True)  
    price_per_night = models.FloatField(blank=True, null=True)  
    amenities = models.TextField(blank=True)

    def __str__(self):
        return self.room_type_name  

class Room_Details(models.Model):
    Detail_ID = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, blank=True, null=True)  
    room_type = models.ForeignKey('Rooms_Type', on_delete=models.CASCADE, blank=True, null=True)  
    price = models.FloatField(blank=True, null=True)
    available_Rooms = models.CharField(choices=[("Yes", "Yes"), ("No", "No")], max_length=3, blank=True)  

    def __str__(self):
        return f"{self.room_type} - {self.hotel.Name}"  

class Amenities(models.Model):
    Hotel_ID = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    Room_id = models.ForeignKey(Room_Details, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    price = models.FloatField(blank=True, null=True)
    is_chargeable = models.CharField(choices=[("Yes", "Yes"), ("No","No")], blank=True, max_length=3)
    other_amenities = models.TextField(blank=True)

    def __str__(self):
        return self.Name

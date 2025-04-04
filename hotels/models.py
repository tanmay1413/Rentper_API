from django.db import models

class Hotel(models.Model):
    Hotel_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, blank=True)
    Price = models.CharField(max_length=200, blank=True)
    Description = models.TextField(blank=True)
    Room_Type = models.ForeignKey('Rooms_Type', on_delete=models.CASCADE, blank=True, null=True)
    Total_No_of_Rooms = models.IntegerField(blank=True, null=True)
    Safety_Features = models.TextField(blank=True)
    Address = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100, blank=True)
    Zip_code = models.IntegerField(blank=True, null=True)
    City = models.CharField(max_length=200, blank=True)
    Nearby_mark = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Name  

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
    Description = models.CharField(max_length=250, blank=True)    
    Occupancy_limit = models.IntegerField(blank=True, null=True)
    Types_of_bed = models.CharField(max_length=200, choices=TYPES, blank=True)  
    Price_Per_Night = models.FloatField(blank=True, null=True)  
    Amenities = models.TextField(blank=True)

    def __str__(self):
        return self.room_type_name  

class Room_Details(models.Model):
    Detail_ID = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, blank=True, null=True)  
    room_type = models.ForeignKey('Rooms_Type', on_delete=models.CASCADE, blank=True, null=True)  
    Price = models.FloatField(blank=True, null=True)
    Available_Rooms = models.CharField(choices=[("Yes", "Yes"), ("No", "No")], max_length=3, blank=True)  

    def __str__(self):
        return f"{self.room_type.room_type_name} - {self.hotel.Name}"  

class Amenities(models.Model):
    ID = models.AutoField(primary_key=True)
    Hotel_ID = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    Room_id = models.ForeignKey(Room_Details, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=200, blank=True)
    Price = models.FloatField(blank=True, null=True)
    Is_chargeable = models.CharField(choices=[("Yes", "Yes"), ("No","No")], blank=True, max_length=3)
    Other_amenities = models.TextField(blank=True)

    def __str__(self):
        return self.Name

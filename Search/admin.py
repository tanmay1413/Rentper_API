from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Booking)
admin.site.register(BookingAmenity)
admin.site.register(Payment)
admin.site.register(Guest)


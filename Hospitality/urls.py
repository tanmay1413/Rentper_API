
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Account.urls')),
    path('hotel_api/',include('hotels.urls')),
    path('media_api/',include('Media.urls'))
]

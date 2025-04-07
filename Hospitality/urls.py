
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('Account.urls')),
    path('hotel_api/',include('hotels.urls')),
    path('media_api/',include('Media.urls'))
]

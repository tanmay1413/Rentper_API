
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('hotels/',include('hotels.urls')),
    path('gallery/',include('gallery.urls')),
    path('pricing-payments/',include('pricing_payments.urls')),
    path('policies/',include('policies.urls')),
    path('documents/',include('documents.urls')),
    path('search/',include('Search.urls'))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include, re_path
from .views import CustomRegisterView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    # dj-rest-auth core and registration
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    # path("api/auth/custom-registration/", CustomRegisterView.as_view(), name="custom_register"),

    # Corrected password reset confirm with uid and token in the URL
    re_path(
        r"^api/auth/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

    # Allauth
    path("api/", include("allauth.urls")),
]

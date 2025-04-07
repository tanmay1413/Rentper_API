# Account/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ("email","profile_photo","first_name" ,"phone_number", "role", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "role")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Personal Info", {"fields": ("phone_number", "role","first_name" )}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone_number", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email","phone_number")
    ordering = ("email","role")

admin.site.register(CustomUser, CustomUserAdmin)

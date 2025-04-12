from dj_rest_auth.serializers import UserDetailsSerializer  
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email



class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'name', 'contact', 'profile_photo')



class CustomRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        setup_user_email(request, user, [])
        return user
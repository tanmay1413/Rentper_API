from .models import CustomUser

from rest_framework import serializers
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields =['id','email','phone_number','profile_photo' ,'first_name', 'role','password']
    extra_kwargs = {'password': {'write_only': True},
                    'role': {'read_only': True}}

  
  
  def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
      
  def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
      
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Invalid credentials")
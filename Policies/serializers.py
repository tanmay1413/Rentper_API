from rest_framework import serializers
from .models import Policies

class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Policies
        fields='__all__'
        
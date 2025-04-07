from .models import Media
from rest_framework import serializers

class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Media
        fields='__all__'
    
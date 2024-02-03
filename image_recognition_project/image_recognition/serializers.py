
from rest_framework import serializers
from .models import RecognizedImage

class RecognizedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizedImage
        fields = ('id', 'image', 'prediction')

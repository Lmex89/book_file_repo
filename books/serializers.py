from rest_framework import serializers
from .models import ImgPortada

class ImgPortadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImgPortada
        fields = '__all__'

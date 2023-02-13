from rest_framework import serializers
from .models import ImgPortada, Categorias


class ImgPortadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgPortada
        fields = "__all__"
        depth = 1


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from models import ImgPortada
from serializers import ImgPortadaSerializer

class ImgPortadaView(generics.RetrieveAPIView):
    queryset = ImgPortada.objects.all()
    serializer_class = ImgPortadaSerializer
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

from django.urls import  path
from views import ImgPortadaView

url_portada = [
    path('portada/<uuid:pk>',
         ImgPortadaView.as_view()),
]
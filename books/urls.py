from django.urls import  path
from views import ImgPortadaView

urlpatterns = [
    path('portada/<uuid:pk>',
         ImgPortadaView.as_view()),
]
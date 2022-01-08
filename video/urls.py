from django.urls import path
from .views import ListaVideo, DetailVideo

urlpatterns = [
    path('videos/', ListaVideo.as_view(), name='lista-video'),
    path('videos/<pk>', DetailVideo.as_view(), name='detail-video')
]

from email.policy import default
from django.urls import path

from Dispositivo.api.views import DispositivoViewSet, DispositivoDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',DispositivoViewSet)
  
urlpatterns = [
    path("/<int:pk>/", DispositivoDetailView.as_view()),
    path("/<str:tipo>/", DispositivoDetailView.as_view()),
]+router.urls
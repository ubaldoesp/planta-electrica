from django.db import router
from django.urls import path

from bitacora.api.views import BitacoraView, BitacoraDetailView, BitacoraEnergyView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',BitacoraView)

urlpatterns = [
    path("/<int:pk>/", BitacoraDetailView.as_view()),
    path("/<str:tipo_dispositivo>/", BitacoraDetailView.as_view()),
    path("/<int:id_dispositivo>/energy/", BitacoraEnergyView.as_view()),
]+router.urls
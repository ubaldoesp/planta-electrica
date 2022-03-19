from django.db import router
from django.urls import path

from bitacora.api.views import BitacoraView, BitacoraDetailView, BitacoraEnergyView


urlpatterns = [
    path("",BitacoraView.as_view()),
    path("/<int:pk>/", BitacoraDetailView.as_view()),
    path("/<str:tipo_dispositivo>/", BitacoraDetailView.as_view()),
    path("/<int:id_dispositivo>/energy/", BitacoraEnergyView.as_view()),
]
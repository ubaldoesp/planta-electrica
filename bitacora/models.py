from django.db import models

from Dispositivo.models import Dispositivo


class Bitacora(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    potencia = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

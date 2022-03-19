from random import choices
from sqlite3 import Timestamp
from django.db import models
# Create your models here.

class Dispositivo(models.Model):
    
    class Tipos(models.IntegerChoices):
        celda=0
        aerogenerador=1
        turbina_hidroelectrica=2
        
    class Status(models.IntegerChoices):
        operacion= 0
        mantenimiento = 1
    
    nombre= models.CharField(max_length=100)
    tipodispositivo= models.IntegerField(choices=Tipos.choices)
    potencia_actual= models.FloatField(default=0)
    status=models.IntegerField(choices=Status.choices)
    date_creation= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)

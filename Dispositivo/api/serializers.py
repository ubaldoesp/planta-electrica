from Dispositivo.models import Dispositivo
from rest_framework.serializers import ModelSerializer

class DispositivoSerializer(ModelSerializer):
    
    class Meta:
        model= Dispositivo 
        fields = '__all__'


from rest_framework import serializers

from Dispositivo.api.serializers import DispositivoSerializer
from bitacora.models import Bitacora
from Dispositivo.models import Dispositivo


class BitacoraSerializer(serializers.ModelSerializer):

    def validate_dispositivo(self, dispositivo):
        print(f"validating {dispositivo.status} {type(dispositivo.status)}")
        if dispositivo.status == 1:
            raise serializers.ValidationError(f"Dispositivo en 'mantenimiento', por favor actualizar a 'operacion'")
        return dispositivo
        
    

    class Meta:
        model = Bitacora
        fields = '__all__'

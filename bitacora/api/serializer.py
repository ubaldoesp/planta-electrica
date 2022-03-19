from rest_framework import serializers

from Dispositivo.api.serializers import DispositivoSerializer
from bitacora.models import Bitacora
from Dispositivo.models import Dispositivo


class BitacoraSerializer(serializers.ModelSerializer):
    dispositivo = serializers.PrimaryKeyRelatedField(queryset=Dispositivo.objects.all())
    timestamp = serializers.DateTimeField(read_only=True)

    def validate_dispositivo(self, dispositivo):
        print(f"validating {dispositivo.status} {type(dispositivo.status)}")
        if dispositivo.status == 1:
            raise serializers.ValidationError(f"Dispositivo en 'mantenimiento', por favor actualizar a 'operacion'")
            
    def create(self, validated_data):
        print("`"*20)
        print(validated_data)

    class Meta:
        model = Bitacora
        fields = '__all__'

from Dispositivo.api.serializers import DispositivoSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from Dispositivo.models import Dispositivo

class DispositivoViewSet(ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class DispositivoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

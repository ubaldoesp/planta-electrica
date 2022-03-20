from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from bitacora.models import Bitacora
from bitacora.api.serializer import BitacoraSerializer


class BitacoraView(ListCreateAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BitacoraDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer


class BitacoraEnergyView(RetrieveAPIView):

    def get_queryset(self, request, *args, **kwargs):
        id_dispositivo = self.kwargs["id_dispositivo"]
        return Bitacora.objects.filter(dispositivo=id_dispositivo)


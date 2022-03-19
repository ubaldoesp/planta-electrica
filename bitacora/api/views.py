from django.db.models import Sum
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from bitacora.models import Bitacora
from bitacora.api.serializer import BitacoraSerializer


class BitacoraView(ModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
    
    def perform_create(self, serializer):
        print(serializer.data)
        print(serializer.validated_data)
        print("<"*20)
        serializer.save()

    def create(self, request, *args, **kwargs):
        print("#"*20)
        print(f"data: {request.data}")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(">"*20)
        self.perform_create(serializer)
        print("-"*20)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BitacoraDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer


class BitacoraEnergyView(RetrieveAPIView):

    def get_queryset(self, request, *args, **kwargs):
        id_dispositivo = self.kwargs["id_dispositivo"]
        return Bitacora.objects.filter(dispositivo=id_dispositivo)

    def retrieve(self, request, *args, **kwargs):
        potencia_sum = self.get_queryset().aggregate(Sum("potencia"))["potencia__sum"]
        return Response({"id_dispositivo": id_dispositivo, "energia": potencia_sum})


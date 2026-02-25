from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..models.animal_model import MascotaPersonal
from ..serializers.animales_serializers import MascotaPersonalSerializer


class MascotaPersonalListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mascotas = MascotaPersonal.objects.filter(propietario=request.user)
        serializer = MascotaPersonalSerializer(mascotas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MascotaPersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(propietario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
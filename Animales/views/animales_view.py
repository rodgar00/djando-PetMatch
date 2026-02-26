from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from Animales.models import Animal, Encontrados, Perdidos, Favoritos
from Animales.serializers import AdoptadoSerializer, EncontradoSerializer, PerdidoSerializer, FavoritoSerializer, MascotaPersonalSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..models.animal_model import MascotaPersonal

class AdoptadoListAPIView(APIView):
    def get(self, request):
        animales = Animal.objects.all()
        serializer = AdoptadoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

class EncontradoListAPIView(APIView):
    def get(self, request):
        animales = Encontrados.objects.all()
        serializer = EncontradoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

class PerdidoListAPIView(APIView):
    def get(self, request):
        animales = Perdidos.objects.all()
        serializer = PerdidoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)


class FavoritoListAPIView(APIView):

    def delete(self, request):
        # Obtenemos los parámetros de la URL (Query Params)
        nombre = request.query_params.get('nombre')
        duenyo = request.query_params.get('duenyo')

        if not nombre or not duenyo:
            return Response(
                {"error": "Se requiere nombre y dueño para eliminar"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Buscamos el favorito que coincida
        favorito = Favoritos.objects.filter(nombre=nombre, duenyo=duenyo).first()

        if favorito:
            favorito.delete()
            return Response({"message": "Eliminado de favoritos"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "No se encontró el animal en favoritos"}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        animales = Favoritos.objects.all()
        serializer = FavoritoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):

        serializer = FavoritoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MascotaPersonalListAPIView(generics.ListCreateAPIView):
    queryset = MascotaPersonal.objects.all()
    serializer_class = MascotaPersonalSerializer
    permission_class = [AllowAny]
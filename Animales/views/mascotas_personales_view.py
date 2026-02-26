from rest_framework import generics
from rest_framework.permissions import AllowAny  # Importa esto
from ..models.animal_model import MascotaPersonal  # Ajusta según tu modelo real
from ..serializers.animales_serializers import MascotaPersonalSerializer


class MascotaPersonalListAPIView(generics.ListCreateAPIView):
    queryset = MascotaPersonal.objects.all()
    serializer_class = MascotaPersonalSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Para pruebas: devuelve todo.
        # Si quieres que sea privado después, aquí filtrarás por self.request.user
        return MascotaPersonal.objects.all()

    def perform_create(self, serializer):
        # Si no hay usuario logueado (Android), lo asignamos como None
        # (Asegúrate de que en tu modelo el campo 'duenyo' permita null=True)
        if self.request.user.is_authenticated:
            serializer.save(duenyo=self.request.user)
        else:
            serializer.save()
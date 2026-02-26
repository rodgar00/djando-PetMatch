from rest_framework import generics, permissions

from rest_framework.permissions import AllowAny # Importa esto

from ..models.animal_model import MascotaPersonal # Ajusta según tu modelo real

from ..serializers.animales_serializers import MascotaPersonalSerializer

class MascotaPersonalListAPIView(generics.ListCreateAPIView):
    serializer_class = MascotaPersonalSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        # Capturamos el email de la URL: /api/mascotas_personales/?email=piero@gmail.com
        email_usuario = self.request.query_params.get('email', None)

        if email_usuario:
            # Filtramos por el email del propietario
            return MascotaPersonal.objects.filter(propietario__email=email_usuario)

        # Si es un invitado (no hay email), devolvemos lista vacía
        return MascotaPersonal.objects.none()

    def perform_create(self, serializer):
        # Al crear desde la app, buscaremos al usuario por el email enviado
        # o lo dejamos como None si prefieres manejar la asignación manual
        serializer.save()
from rest_framework import generics, permissions

from rest_framework.permissions import AllowAny # Importa esto

from ..models.animal_model import MascotaPersonal # Ajusta según tu modelo real

from ..serializers.animales_serializers import MascotaPersonalSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

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
        # 1. Intentamos obtener el email de los datos enviados (POST)
        email_propietario = self.request.data.get('email_propietario')

        if email_propietario:
            try:
                # 2. Buscamos al usuario que tenga ese email
                usuario = User.objects.get(email=email_propietario)
                # 3. Guardamos la mascota asignándole ese usuario
                serializer.save(propietario=usuario)
            except User.DoesNotExist:
                # Si el email no existe, guardamos sin propietario o manejamos el error
                serializer.save()
        else:
            # Si no viene email, guardamos normal (posiblemente como None)
            serializer.save()
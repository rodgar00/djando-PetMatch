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
        email_usuario = self.request.query_params.get('email', None)

        if email_usuario:
            return MascotaPersonal.objects.filter(propietario__email=email_usuario)

        return MascotaPersonal.objects.none()

    def perform_create(self, serializer):
        email_propietario = self.request.data.get('email_propietario')

        if email_propietario:
            try:
                usuario = User.objects.get(email=email_propietario)
                serializer.save(propietario=usuario)
            except User.DoesNotExist:
                serializer.save()
        else:
            serializer.save()
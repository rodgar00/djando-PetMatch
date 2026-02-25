from django.urls import path
from .views import AdoptadoListAPIView, EncontradoListAPIView, PerdidoListAPIView, FavoritoListAPIView
from .views.crear_animal import CrearAnimalAPIView
from .views.mascotas_personales_view import MascotaPersonalListAPIView

urlpatterns = [
    path('adoptados/', AdoptadoListAPIView.as_view(), name='adoptados-list'),
    path('encontrados/', EncontradoListAPIView.as_view(), name='encontrados-list'),
    path('perdidos/', PerdidoListAPIView.as_view(), name='perdidos-list'),
    path('favoritos/', FavoritoListAPIView.as_view(), name='favoritos-list'),
    path('crear_animal/', CrearAnimalAPIView.as_view(), name='crear_animal'),  # POST
    path('mascotas_personales/', MascotaPersonalListAPIView.as_view(), name='mascotas-personales'),

]



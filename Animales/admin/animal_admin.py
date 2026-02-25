from django.contrib import admin
from Animales.models import Animal, Encontrados, Perdidos, Favoritos, MascotaPersonal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duenyo", "edad", "localizacion", "categoria", "slug")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "duenyo")

@admin.register(Encontrados)
class EncontradosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "localizacion", "categoria", "slug")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "localizacion")

@admin.register(Perdidos)
class PerdidosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duenyo", "edad", "localizacion", "categoria", "slug")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "duenyo")

@admin.register(Favoritos)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duenyo", "edad", "localizacion", "categoria", "slug")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "duenyo")
@admin.register(MascotaPersonal)
class MascotaPersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "propietario", "fecha_creacion")
    search_fields = ("nombre",)
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings


class Animal(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    duenyo = models.CharField(max_length=200, blank=True, null=True)
    edad = models.IntegerField(verbose_name="Edad", default=1)
    localizacion = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='animals/', null=True, blank=True)
    es_refugio = models.BooleanField(default=False)
    categoria = models.CharField(
        max_length=50,
        choices=[("Perro", "Perro"), ("Gato", "Gato"), ("Otro", "Otro")],
        default="Otro"
    )
    raza = models.CharField(default="sin raza", max_length=200, blank=False, null=False)

    class Meta:
        db_table = 'adoptados'
        ordering = ['nombre']
        verbose_name = 'Adoptados'
        verbose_name_plural = 'Adoptados'

    def __str__(self):
        return f"{self.nombre} [{self.categoria}]"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nombre)
            slug = base_slug
            contador = 1

            while Animal.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{contador}"
                contador += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Encontrados(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    localizacion = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='animals/', null=True, blank=True)
    categoria = models.CharField(
        max_length=50,
        choices=[("Perro", "Perro"), ("Gato", "Gato"), ("Otro", "Otro")],
        default="Otro"
    )
    raza = models.CharField(default="sin raza", max_length=200, blank=False, null=False)

    class Meta:
        db_table = 'encontrados'
        ordering = ['nombre']
        verbose_name = 'Encontrado'
        verbose_name_plural = 'Encontrados'

    def __str__(self):
        return f"{self.nombre} [{self.categoria}]"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nombre)
            slug = base_slug
            contador = 1

            while Encontrados.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{contador}"
                contador += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Perdidos(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    duenyo = models.CharField(max_length=200, blank=True, null=True)
    edad = models.IntegerField(verbose_name="Edad", default=1)
    localizacion = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='animals/', null=True, blank=True)
    es_refugio = models.BooleanField(default=False)
    categoria = models.CharField(
        max_length=50,
        choices=[("Perro", "Perro"), ("Gato", "Gato"), ("Otro", "Otro")],
        default="Otro"
    )
    raza = models.CharField(default="sin raza", max_length=200, blank=False, null=False)

    class Meta:
        db_table = 'perdidos'
        ordering = ['nombre']
        verbose_name = 'Perdido'
        verbose_name_plural = 'Perdidos'

    def __str__(self):
        return f"{self.nombre} [{self.categoria}]"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nombre)
            slug = base_slug
            contador = 1

            while Perdidos.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{contador}"
                contador += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Favoritos(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    duenyo = models.CharField(max_length=200, blank=True, null=True)
    edad = models.IntegerField(verbose_name="Edad", default=1)
    localizacion = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='animals/', null=True, blank=True)
    es_refugio = models.BooleanField(default=False)
    raza = models.CharField(default="sin raza", max_length=200, blank=False, null=False)
    categoria = models.CharField(
        max_length=50,
        choices=[("Perro", "Perro"), ("Gato", "Gato"), ("Otro", "Otro")],
        default="Otro"
    )

    class Meta:
        db_table = 'favoritos'
        ordering = ['nombre']
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = [['nombre', 'duenyo', 'localizacion']] #Esto hace que no se repita el animal una vez lo guardas en favorito

    def __str__(self):
        return f"{self.nombre} [{self.categoria}]"

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo si es una creación nueva
            existe = Favoritos.objects.filter(
                nombre=self.nombre,
                duenyo=self.duenyo,
                localizacion=self.localizacion
            ).exists()
            if existe:
                raise ValidationError("Este animal ya está en tus favoritos.")
        if not self.slug:
            base_slug = slugify(self.nombre)
            slug = base_slug
            contador = 1

            while Favoritos.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{contador}"
                contador += 1

            self.slug = slug

        super().save(*args, **kwargs)




class MascotaPersonal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=100)
    # ¡Asegúrate de que esta línea exista!
    imagen = models.ImageField(upload_to='mascotas/', null=True, blank=True)

    propietario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,  # <--- ESTO permite que la DB acepte vacíos
        blank=True
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

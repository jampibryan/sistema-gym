from django.db import models
from django.contrib.auth.models import User

class TipoGenero(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Disciplina(models.Model):
    descripcionD = models.CharField(max_length=100)  # Requerido

    def __str__(self):
        return self.descripcionD

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fotoPerfil = models.ImageField(upload_to='imagenes/perfil', null=False)  # Requerido
    username = models.CharField(max_length=50)  # Requerido
    nombre = models.CharField(max_length=50)  # Requerido
    apellidos = models.CharField(max_length=50)  # Requerido
    genero = models.ForeignKey(TipoGenero, on_delete=models.CASCADE)  # Requerido
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, null=False)  # Requerido

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
        
        
class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)  # Requerido
    fechaPost = models.DateTimeField(auto_now_add=True)  # Requerido, pero se asigna automáticamente

    def __str__(self):
        return f"Publicación de {self.usuario} el {self.fechaPost}"


class ImagenMensaje(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes/post', null=False)  # Requerido
    mensaje = models.TextField(blank=True)  # No requerido

    def __str__(self):
        return f"Imagen de {self.publicacion.usuario} con mensaje"
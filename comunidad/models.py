from django.db import models
from django.contrib.auth.models import User

class TipoGenero(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero = models.ForeignKey(TipoGenero, on_delete=models.CASCADE)  # Requerido
    nombre = models.CharField(max_length=100)  # Requerido
    apellidos = models.CharField(max_length=100)  # Requerido

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Disciplina(models.Model):
    descripcionDisciplina = models.CharField(max_length=100)  # Requerido

    def __str__(self):
        return self.descripcionDisciplina

class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)  # Requerido
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)  # Requerido
    fechaPost = models.DateTimeField(auto_now_add=True)  # Requerido, pero se asigna automáticamente
    imagen = models.ImageField(upload_to='imagenes/', null=False)  # Requerido
    mensaje = models.TextField(blank=True)  # No requerido

    def __str__(self):
        return f"Publicación de {self.usuario} en {self.disciplina}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
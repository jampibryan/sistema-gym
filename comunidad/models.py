from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Disciplina(models.Model):
    descripcionDisciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcionDisciplina
    
    
class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', null=False)
    mensaje = models.TextField(null=False)

    def __str__(self):
        return f"Publicación de {self.usuario} en {self.disciplina}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

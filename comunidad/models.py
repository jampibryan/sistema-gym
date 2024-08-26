from django.db import models

# Create your models here.

class TipoGenero(models.Model):
    descripcionG = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcionG
    
    
class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()  # Esto asegura que la edad sea un número positivo
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    tipo_genero = models.ForeignKey(TipoGenero, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

class Disciplina(models.Model):
    descripcionDisciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcionDisciplina
    
    
class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', null=False)
    mensaje = models.TextField(null=False)

    def __str__(self):
        return f"Publicación de {self.usuario} en {self.disciplina}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

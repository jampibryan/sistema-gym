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
    
    
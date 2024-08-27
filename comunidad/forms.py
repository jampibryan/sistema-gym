from django import forms

from .models import Disciplina, Publicacion

# Define un formulario automáticamente basado en el modelo Libro. 


class DisciplinaForm(forms.ModelForm): 
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'descripcionDisciplina': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción'
            })
        }
        labels = {
            'descripcionDisciplina': ''
        }
        
        
class PublicacionForm(forms.ModelForm): 
    class Meta:
        model = Publicacion
        fields = '__all__'
        fields = ['disciplina', 'imagen', 'mensaje']  # Especifica los campos que quieres incluir
      
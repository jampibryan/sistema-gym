from django import forms

from .models import TipoGenero, Usuario, Disciplina, Publicacion

# Define un formulario automáticamente basado en el modelo Libro. 
class GeneroForm(forms.ModelForm): 
    class Meta:
        model = TipoGenero
        fields = '__all__'

class UsuarioForm(forms.ModelForm): 
    class Meta:
        model = Usuario
        fields = '__all__'

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
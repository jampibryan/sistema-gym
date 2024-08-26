from django import forms

from .models import TipoGenero, Usuario

# Define un formulario automáticamente basado en el modelo Libro. 
class GeneroForm(forms.ModelForm): 
    class Meta:
        model = TipoGenero
        fields = '__all__'

class UsuarioForm(forms.ModelForm): 
    class Meta:
        model = Usuario
        fields = '__all__'
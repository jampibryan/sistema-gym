from django import forms
from .models import Usuario, TipoGenero, Disciplina, Publicacion
from django.contrib.auth import authenticate
from django.contrib.auth.models import User  # Importa el modelo User

# Formulario de autenticación personalizado
class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username_or_email, password=password)
        
        if user is None:
            try:
                user_temp = User.objects.get(email=username_or_email)
                user = authenticate(username=user_temp.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is None:
            raise forms.ValidationError('Invalid login credentials')
        
        self.cleaned_data['user'] = user
        return self.cleaned_data


# Formulario de registro de usuario
class RegistroForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña", required=True)
    genero = forms.ModelChoiceField(queryset=TipoGenero.objects.all(), required=True)
    nombre = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            usuario = Usuario(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellidos=self.cleaned_data['apellidos'],
                genero=self.cleaned_data['genero'],
            )
            usuario.save()

        return user


# Formulario de Disciplina
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
        
        
# Formulario de Publicación
class PublicacionForm(forms.ModelForm): 
    class Meta:
        model = Publicacion
        fields = ['disciplina', 'imagen', 'mensaje']  # Especifica los campos que quieres incluir

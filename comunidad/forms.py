from django import forms
from .models import Usuario, TipoGenero, Disciplina, Publicacion, ImagenMensaje
from django.contrib.auth import authenticate
from django.contrib.auth.models import User  # Importa el modelo User
from django.forms import inlineformset_factory


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
    username = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    fotoPerfil = forms.ImageField(required=True)
    genero = forms.ModelChoiceField(queryset=TipoGenero.objects.all(), required=True)
    disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all(), required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'password2', 'fotoPerfil', 'nombre', 'apellidos', 'genero', 'disciplina']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        # Creando usuario de la tabla User
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        # Creando instancia del modelo Usuario
        usuario = Usuario(
            user=user,
            nombre=self.cleaned_data['nombre'],
            apellidos=self.cleaned_data['apellidos'],
            genero=self.cleaned_data['genero'],
            fotoPerfil=self.cleaned_data['fotoPerfil'],
            disciplina=self.cleaned_data['disciplina'],
        )

        if commit:
            usuario.save()

        return usuario
    


# Formulario de Disciplina
class DisciplinaForm(forms.ModelForm): 
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'descripcionD': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción'
            })
        }
        labels = {
            'descripcionD': ''
        }
        
        
# Formulario de Publicación
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = []

class ImagenMensajeForm(forms.ModelForm):
    class Meta:
        model = ImagenMensaje
        fields = ['imagen', 'mensaje']

ImagenMensajeFormSet = inlineformset_factory(
    # Publicacion, ImagenMensaje, form=ImagenMensajeForm, extra=7, max_num=7, can_delete=False
    Publicacion, ImagenMensaje, form=ImagenMensajeForm, extra=7, max_num=7
)
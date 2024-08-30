from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Disciplina, Publicacion
from .forms import DisciplinaForm, CustomAuthenticationForm, RegistroForm,  PublicacionForm, ImagenMensajeFormSet

# from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    # publicaciones = Publicacion.objects.all()
    # return render(request, 'inicio.html', {'publicaciones': publicaciones})
    return redirect('login')


# DISCIPLINAS

def disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas/index.html', {'disciplinas': disciplinas})

def crearDisciplina(request):
    formulario = DisciplinaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('disciplinas')
    return render(request, 'disciplinas/crear.html', {'formulario' : formulario})

def editarDisciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    formulario = DisciplinaForm(request.POST or None, request.FILES or None, instance=disciplina)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('disciplinas')
    return render(request, 'disciplinas/editar.html', {'formulario': formulario})

def eliminarDisciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    disciplina.delete()
    return redirect('disciplinas')


# PUBLICACIONES

@login_required
def perfilUsuario(request, id):
    user = User.objects.get(id=id)
    
    if request.user.id != id:
        return redirect('login')
    
    publicaciones = Publicacion.objects.filter(usuario=user).prefetch_related('imagenes')
    return render(request, 'perfil.html', {'user': user, 'publicaciones': publicaciones})


    # return render(request, 'publicaciones/index.html', {'user': user, 'publicaciones': publicaciones})



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('perfilUsuario', id = user.id) 
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'register.html', {'form': form})


# LOGOUT
def logout_view(request):
    auth_logout(request)
    return redirect('inicio') 



# CREAR PUBLICACIÓN
@login_required
def crearPublicacion(request):
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST)
        formset = ImagenMensajeFormSet(request.POST, request.FILES)
        
        if publicacion_form.is_valid() and formset.is_valid():
            publicacion = publicacion_form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            formset.instance = publicacion
            formset.save()
            return redirect('perfilUsuario', id=request.user.id)  # Redirige al perfil del usuario
    else:
        publicacion_form = PublicacionForm()
        formset = ImagenMensajeFormSet()

    return render(request, 'post/createPost.html', {
        'publicacion_form': publicacion_form,
        'formset': formset,
        'id' : request.user.id,
    })
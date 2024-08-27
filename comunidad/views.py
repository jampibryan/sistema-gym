from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Disciplina, Publicacion
from .forms import DisciplinaForm, PublicacionForm

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


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
    # Obtén el usuario solicitado
    user = User.objects.get(id=id)
    
    # Verifica que el usuario autenticado tenga permiso para ver el perfil
    if request.user.id != id:
        # Redirige a una página de acceso denegado o muestra un mensaje de error
        return redirect('inicio')  # Redirige a una página de inicio o error
    
    publicaciones = Publicacion.objects.filter(usuario = user)
    return render(request, 'publicaciones/index.html', {'user': user, 'publicaciones': publicaciones})


# def crearPublicacion(request):
#     usuario_id = request.session.get('usuario_id')
    
#     if not usuario_id:
#         return redirect('perfilUsuario', id=usuario_id)
    
#     usuario = Usuario.objects.get(id=usuario_id)
#     if request.method == 'POST':
#         formulario = PublicacionForm(request.POST, request.FILES)
#         if formulario.is_valid():
#             publicacion = formulario.save(commit=False)
#             publicacion.usuario = usuario
#             publicacion.save()
#             return redirect('perfilUsuario', id = usuario_id)
#     else:
#         formulario = PublicacionForm()

#     return render(request, 'publicaciones/crear.html', {'formulario': formulario, 'usuario': usuario})


@login_required
def crearPublicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user  # Asignar el usuario autenticado
            publicacion.save()
            return redirect('perfilUsuario', id=request.user.id)
    else:
        form = PublicacionForm()
    
    return render(request, 'publicaciones/crear.html', {'formulario': form})

# AUTENTICACIÓN

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Correcto uso de login
            return redirect('perfilUsuario', id=user.id)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Correcto uso de login
            return redirect('perfilUsuario', id=user.id)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# LOGOUT
def logout_view(request):
    auth_logout(request)
    return redirect('inicio')  # Redirige a la página de login o a la página principal después de cerrar sesión
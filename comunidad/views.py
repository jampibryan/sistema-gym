from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Disciplina, Publicacion
from .forms import DisciplinaForm, CustomAuthenticationForm, RegistroForm, PublicacionForm, ImagenMensajeFormSet


# Create your views here.

def inicio(request):
    # publicaciones = Publicacion.objects.all()
    # return render(request, 'inicio.html', {'publicaciones': publicaciones})
    return redirect('login')

#LOGIN DE USUARIO

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

#REGISTRO DE USUARIO

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


# PERFIL DE USUARIO

@login_required
def perfilUsuario(request, id):
    user = User.objects.get(id=id)
    
    if request.user.id != id:
        return redirect('login')
    
    publicaciones = Publicacion.objects.filter(usuario=user).prefetch_related('imagenes')
    
    # Verificar si el usuario ya ha hecho una publicación
    publicacion_reciente = publicaciones.exists()
    
    return render(request, 'perfil.html', {
        'user': user,
        'publicaciones': publicaciones,
        'publicacion_reciente': publicacion_reciente 
    })




# CREAR PUBLICACIÓN
@login_required
def crearPublicacion(request):
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST)
        formset = ImagenMensajeFormSet(request.POST, request.FILES)
        
        if publicacion_form.is_valid() and formset.is_valid():
            has_image = any([form.cleaned_data.get('imagen') for form in formset.forms])
            
            if not has_image:
                messages.error(request, "Debe subir almenos 1 imagen.")
            else:
                publicacion = publicacion_form.save(commit=False)
                publicacion.usuario = request.user
                publicacion.save()
                formset.instance = publicacion
                formset.save()
                return redirect('perfilUsuario', id=request.user.id)
    else:
        publicacion_form = PublicacionForm()
        formset = ImagenMensajeFormSet()

    return render(request, 'post/createPost.html', {
        'publicacion_form': publicacion_form,
        'formset': formset,
        'id': request.user.id,
    })
    
    
    
# EDITAR PUBLICACIÓN

def editarPublicacion(request, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)
    
    if request.user != publicacion.usuario:
        return redirect('perfilUsuario', id=request.user.id)
    
    if request.method == 'POST':
        formset = ImagenMensajeFormSet(request.POST, request.FILES, instance=publicacion)
        if formset.is_valid():
            formset.save()
            return redirect('perfilUsuario', id=request.user.id)
    else:
        formset = ImagenMensajeFormSet(instance=publicacion)
    
    return render(request, 'post/editPost.html', {'formset': formset, 'publicacion': publicacion})


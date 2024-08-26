from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import TipoGenero, Usuario, Disciplina, Publicacion
from .forms import GeneroForm, UsuarioForm, DisciplinaForm, PublicacionForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


# GÉNERO

def generos(request):
    generos = TipoGenero.objects.all()
    return render(request, 'generos/index.html', {'generos': generos})

def crearGenero(request):
    formulario = GeneroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('generos')
    return render(request, 'generos/crear.html', {'formulario' : formulario})

def editarGenero(request, id):
    genero = TipoGenero.objects.get(id=id)
    formulario = GeneroForm(request.POST or None, request.FILES or None, instance=genero)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('generos')
    return render(request, 'generos/editar.html', {'formulario': formulario})

def eliminarGenero(request, id):
    genero = TipoGenero.objects.get(id=id)
    genero.delete()
    return redirect('generos')


# USUARIOS

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

def crearUsuario(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario' : formulario})

def editarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario': formulario})

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')


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

def perfilUsuario(request, id):
    # Obtén el usuario
    usuario = Usuario.objects.get(id=id)
    
    # Guarda el ID del usuario en la sesión
    request.session['usuario_id'] = id
    
    # Obtén todas las publicaciones relacionadas con el usuario
    publicaciones = Publicacion.objects.filter(usuario=usuario)
    
    # Pasa el usuario y las publicaciones al template
    return render(request, 'publicaciones/index.html', {'usuario': usuario, 'publicaciones': publicaciones})


def crearPublicacion(request):
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        # Si por alguna razón no está el usuario_id en la sesión, redirigir a algún lugar
        return redirect('perfilUsuario', id=usuario_id)
    
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        formulario = PublicacionForm(request.POST, request.FILES)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.usuario = usuario
            publicacion.save()
            return redirect('perfilUsuario', id = usuario_id)
    else:
        formulario = PublicacionForm()

    return render(request, 'publicaciones/crear.html', {'formulario': formulario, 'usuario': usuario})



    # formulario = PublicacionForm(request.POST or None, request.FILES or None)
    # if formulario.is_valid():
    #     formulario.save()
    #     return redirect('perfilUsuario', id=id)
    # return render(request, 'publicaciones/crear.html', {'formulario' : formulario, 'id': id})
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import TipoGenero, Usuario, Disciplina
from .forms import GeneroForm, UsuarioForm, DisciplinaForm

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
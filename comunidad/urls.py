from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # GÉNEROS
    path('generos', views.generos, name='generos'),  
    path('generos/crear', views.crearGenero, name='crearGenero'),    
    path('generos/editar/<int:id>', views.editarGenero, name='editarGenero'),   
    path('generos/<int:id>', views.eliminarGenero, name='eliminarGenero'),    

    # USUARIOS 
    path('usuarios', views.usuarios, name='usuarios'),  
    path('usuarios/crear', views.crearUsuario, name='crearUsuario'),    
    path('usuarios/editar/<int:id>', views.editarUsuario, name='editarUsuario'),   
    path('usuarios/<int:id>', views.eliminarUsuario, name='eliminarUsuario'),    
      
    # DISCIPLINAS
    path('disciplinas', views.disciplinas, name='disciplinas'),  
    path('disciplinas/crear', views.crearDisciplina, name='crearDisciplina'),    
    path('disciplinas/editar/<int:id>', views.editarDisciplina, name='editarDisciplina'),   
    path('disciplinas/<int:id>', views.eliminarDisciplina, name='eliminarDisciplina'),    
    
    
     
]
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('generos', views.generos, name='generos'),  
    path('generos/crear', views.crearGenero, name='crearGenero'),    
    path('generos/editar/<int:id>', views.editarGenero, name='editarGenero'),   
    path('generos/<int:id>', views.eliminarGenero, name='eliminarGenero'),    

    path('usuarios', views.usuarios, name='usuarios'),  
    path('usuarios/crear', views.crearUsuario, name='crearUsuario'),    
    path('usuarios/editar/<int:id>', views.editarUsuario, name='editarUsuario'),   
    path('usuarios/<int:id>', views.eliminarUsuario, name='eliminarUsuario'),    
    
      
]

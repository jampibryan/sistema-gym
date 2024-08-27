from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
      
    # DISCIPLINAS
    path('disciplinas', views.disciplinas, name='disciplinas'),  
    path('disciplinas/crear', views.crearDisciplina, name='crearDisciplina'),    
    path('disciplinas/editar/<int:id>', views.editarDisciplina, name='editarDisciplina'),   
    path('disciplinas/<int:id>', views.eliminarDisciplina, name='eliminarDisciplina'),    
    
    # PUBLICACIONES
    path('perfil/<int:id>', views.perfilUsuario, name='perfilUsuario'),
    path('publicaciones/crear', views.crearPublicacion, name='crearPublicacion'),    
    

    # AUTENTICACIÓN
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
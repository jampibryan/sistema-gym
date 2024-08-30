from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # AUTENTICACIÓN
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
      
    #PERFIL USUARIO
    path('perfil/<int:id>', views.perfilUsuario, name='perfilUsuario'),
    path('publicacion/crear', views.crearPublicacion, name='crearPublicacion'),    

      
    # DISCIPLINAS
    # path('disciplinas', views.disciplinas, name='disciplinas'),  
    # path('disciplinas/crear', views.crearDisciplina, name='crearDisciplina'),    
    # path('disciplinas/editar/<int:id>', views.editarDisciplina, name='editarDisciplina'),   
    # path('disciplinas/<int:id>', views.eliminarDisciplina, name='eliminarDisciplina'),    
    
    # PUBLICACIONES
    # path('perfil/<int:id>', views.perfilUsuario, name='perfilUsuario'),
    # path('publicaciones/crear', views.crearPublicacion, name='crearPublicacion'),    
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from . import views
from django.urls import path
from .views import home, news, registrar, recuperasPass, perfilUsuario, listarNoticia, resenaSwitch, resena, resenaXbox, resenaPlay, about
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home,name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('registrar/', registrar, name='registrar'),
    path('perfilUsuario/', perfilUsuario, name='perfilUsuario'),
    path('recuperasPass/', recuperasPass, name='recuperasPass'),
    path('news/', news, name='news'),
    path('listarNoticia/', listarNoticia, name='listarNoticia'),
    path('resenaSwitch/', resenaSwitch, name='resenaSwitch'),
    path('resenaXbox/', resenaXbox, name='resenaXbox'),
    path('resenaPlay/', resenaPlay, name='resenaPlay'),
    path('resena/', resena, name='resena'),
    path('about/', about, name='about'),
    #VIEWS
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
] 
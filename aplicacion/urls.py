from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('usuario/', usuario, name="usuario"),
    path('alojamientos/', alojamiento, name="alojamiento"),
    path('review/', review, name="review"),
    path('ciudad_alojamientos/', ciudades, name="ciudad_alojamientos"),
    #_________________________________________________ URL de cada alojamiento en especifico
    path('alojamiento/<int:alojamiento_id>/', detalle_alojamiento, name='detalle_alojamiento'),
    #_________________________________________________ URLs de los formularios
    path('nuevo_review/', nuevo_review, name="nuevo_review"),
    path('nuevo_usuario/', nuevo_usuario, name="nuevo_usuario"),
    path('nueva_ciudad/', nueva_ciudad, name="nueva_ciudad"),
    #_________________________________________________ CRUD "mis alojamientos"
    path('misAlojamientos/', AlojamientoList.as_view(), name="misAlojamientos"), 
    path('agregarAlojamiento/', AlojamientoCreate.as_view(), name="agregarAlojamiento"), 
    path('actualizarAlojamiento/<int:pk>/', AlojamientoUpdate.as_view(), name="actualizarAlojamiento"), 
    path('eliminarAlojamiento/<int:pk>/', AlojamientoDelete.as_view(), name="eliminarAlojamiento"), 
    #_________________________________________________ CRUD reseñas
    path('todasLasReseñas/',ReviewList.as_view(), name="todasLasReseñas"), 
    path('agregarReseña/', ReviewCreate.as_view(), name="agregarReseña"), 
    path('actualizarReseña/<int:pk>/', ReviewUpdate.as_view(), name="actualizarReseña"), 
    path('eliminarReseña/<int:pk>/', ReviewDelete.as_view(), name="eliminarReseña"),
    #_________________________________________________ CRUD usuarios
    path('todosLosUsuarios/', UsuarioList.as_view(), name="todosLosUsuarios"), 
    path('agregarUsuario/', UsuarioCreate.as_view(), name="agregarUsuario"), 
    path('actualizarUsuario/<int:pk>/', UsuarioUpdate.as_view(), name="actualizarUsuario"), 
    path('eliminarUsuario/<int:pk>/', UsuarioDelete.as_view(), name="eliminarUsuario"),
    #_________________________________________________ CRUD ciudades
    path('todasLasCiudades/', CiudadList.as_view(), name="todasLasCiudades"), 
    path('agregarCiudad/', CiudadCreate.as_view(), name="agregarCiudad"), 
    path('actualizarCiudad/<int:pk>/', CiudadUpdate.as_view(), name="actualizarCiudad"), 
    path('eliminarCiudad/<int:pk>/', CiudadDelete.as_view(), name="eliminarCiudad"),     
    #_________________________________________________ URLs de la búsqueda
    path('buscar_alojamiento/', buscar_alojamiento, name="buscar_alojamiento"),
    path('encontrar_alojamiento/', encontrar_alojamiento, name="encontrar_alojamiento"),
    #_________________________________________________ Login, Logout y Registro
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    #_________________________________________________ URLs del perfil
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    #_________________________________________________ URLs sobre mi
    path('about_me/', views.about_me, name='about_me'),
]

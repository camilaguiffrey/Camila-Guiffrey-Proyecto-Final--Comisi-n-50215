from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, default='')
    telefono = models.IntegerField(default=0)
    nacionalidad = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, unique=True, default='')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='ciudades', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Alojamiento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200, default="No determinado")
    email = models.EmailField(default="example@example.com")    
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='alojamientos', null=True, blank=True)

    def __str__(self):
        return self.titulo       

class Review(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reseña de {self.usuario} para {self.alojamiento}"
    
class Avatar(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='avatar_user')
    imagen = models.ImageField(upload_to="avatars", default=None)

    def __str__(self):
        return self.user.username + ' Avatar'


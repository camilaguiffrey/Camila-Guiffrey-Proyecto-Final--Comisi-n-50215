from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['alojamiento', 'texto']

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ['titulo', 'descripcion', 'ciudad', 'direccion', 'email', 'precio', 'imagen']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'email', 'telefono', 'nacionalidad', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].max_length = Usuario._meta.get_field('password').max_length

class UserEditForm(UserChangeForm):  
    nombre = forms.CharField(label="Nombre/s", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido/s", max_length=50, required=True)
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Teléfono", required=True)

    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "nacionalidad", "telefono"] 

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True) 

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'imagen']

from django.shortcuts import render, get_object_or_404, redirect

from .models import * 
from .forms import *

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

def home(request):
    return render(request, "aplicacion/index.html")

#______________________________________________________ usuarios
@login_required
def usuario(request):
    contexto = {'usuario': Usuario.objects.all()}
    return render(request, "aplicacion/usuario.html", contexto)

@login_required
def nuevo_usuario(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            u_nombre= miForm.cleaned_data.get("nombre")
            u_email = miForm.cleaned_data.get("email")
            usuario = Usuario(nombre=u_nombre, email=u_email)
            usuario.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = UsuarioForm()
    return render(request, "aplicacion/nuevo_usuario.html", {"form": miForm})

#______________________________________________________ reseñas
def review(request):
    return render(request, "aplicacion/review.html")

@login_required
def nuevo_review(request):
    if request.method == "POST":
        miForm = ReviewForm(request.POST)
        if miForm.is_valid():
            r_alojamiento = miForm.cleaned_data.get("alojamiento")
            r_texto = miForm.cleaned_data.get("texto")
            r_usuario = request.user
            review = Review(alojamiento=r_alojamiento, texto=r_texto, usuario=r_usuario)
            review.save()
            return render(request, "aplicacion/index.html")
    else:

        miForm = ReviewForm()
    return render(request, "aplicacion/nuevo_review.html", {"form": miForm})

def lista_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'aplicacion/index.html', {'ciudades': ciudades})

#______________________________________________________ alojamientos
def alojamiento(request):
    contexto = {'alojamiento': Alojamiento.objects.all()}

    return render(request, "aplicacion/alojamiento.html", contexto)

def detalle_alojamiento(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)

    return render(request, 'aplicacion/detalle_alojamiento.html', {'alojamiento': alojamiento})

#_______ CRUD alojamientos
class AlojamientoList(LoginRequiredMixin, ListView):
    model = Alojamiento

    def get_queryset(self):
        user = self.request.user
        queryset = Alojamiento.objects.filter(propietario=user)
        return queryset # utilicé esta función que filtra los alojamientos para mostrar solo aquellos que pertenecen al usuario que está actualmente autenticado como propietario

class AlojamientoCreate(LoginRequiredMixin, CreateView):
    model = Alojamiento
    fields = ['titulo', 'descripcion', 'ciudad', 'direccion', 'email', 'precio', 'imagen']
    success_url = reverse_lazy("alojamiento")
    
    def form_valid(self, form): # Esto es para que el propietario del alojamiento sea el mismo que los esta creando
        form.instance.propietario = self.request.user
        return super().form_valid(form)
    
class AlojamientoUpdate(LoginRequiredMixin, UpdateView):
    model = Alojamiento
    fields = ['titulo', 'descripcion', 'ciudad', 'direccion', 'email', 'precio', 'imagen']
    success_url = reverse_lazy("alojamiento")

class AlojamientoDelete(LoginRequiredMixin, DeleteView):
    model = Alojamiento
    success_url = reverse_lazy("alojamiento")

#_______ CRUD reseñas
class ReviewList(LoginRequiredMixin, ListView):
    model = Review

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['alojamiento', 'texto']
    success_url = reverse_lazy("home")

    def form_valid(self, form): # Para que aparezca el usuario que publico la reseña
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields =['alojamiento', 'texto']
    success_url = reverse_lazy("home")

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy("home")

#_______ CRUD usuarios
class UsuarioList(LoginRequiredMixin, ListView):
    model = Usuario

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'email', 'username', 'telefono', 'nacionalidad','password']
    success_url = reverse_lazy("home")
    
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'email', 'username', 'telefono', 'nacionalidad','password']
    success_url = reverse_lazy("home")

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("home")

#_______ CRUD ciudades
class CiudadList(LoginRequiredMixin, ListView):
    model = Ciudad

class CiudadCreate(LoginRequiredMixin, CreateView):
    model = Ciudad
    fields = ['nombre', 'imagen']
    success_url = reverse_lazy("home")
    
class CiudadUpdate(LoginRequiredMixin, UpdateView):
    model = Ciudad
    fields =['nombre', 'imagen']
    success_url = reverse_lazy("home")

class CiudadDelete(LoginRequiredMixin, DeleteView):
    model = Ciudad
    success_url = reverse_lazy("home")

#_______ buscar alojamientos
def buscar_alojamiento(request):
    return render(request, "aplicacion/buscar_alojamiento.html")

def encontrar_alojamiento(request): # aqui tuve que utilizar otra forma diferente a la que nos enseñaron en clase ya que al tener una clave externa me tiraba error
    if "buscar" in request.GET:
        patron = request.GET["buscar"]
        alojamiento = Alojamiento.objects.filter(ciudad__nombre__icontains=patron)
        contexto = {"alojamiento": alojamiento}
        return render(request, "aplicacion/alojamiento.html", contexto)
    
    contexto = {"alojamiento": Alojamiento.objects.all()}

    return render(request, "aplicacion/alojamiento.html", contexto)

#______________________________________________________ Login, Logout y Registro
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

               #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar


            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})
    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            email = miForm.cleaned_data.get("email")
            username = miForm.cleaned_data.get("username")
            telefono = miForm.cleaned_data.get("telefono")
            nacionalidad = miForm.cleaned_data.get("nacionalidad")
            password = miForm.cleaned_data.get("password1")

            user = Usuario.objects.create_user(username=username, email=email, password=password)
            user.first_name = nombre
            user.last_name = apellido
            user.telefono = telefono
            user.nacionalidad = nacionalidad
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                return f"Ha ocurrido un error"

    else:
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm})

#________________________ Vistas del perfil
@login_required
def editProfile(request): # Editar el perfil
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            usuario = request.user
            usuario.first_name = miForm.cleaned_data.get("nombre")
            usuario.last_name = miForm.cleaned_data.get("apellido")
            usuario.telefono = miForm.cleaned_data.get("telefono")
            usuario.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            usuario.save()
            return redirect(reverse_lazy('home'))
    else:
        usuario = request.user 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm})    

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

#________________________  Modificar avatares
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = Usuario.objects.get(username=request.user)
            # Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} ) 

#______________________________________________________ vistas de Ciudad
def ciudades(request):
    contexto = {'ciudad': Ciudad.objects.all()}
    return render(request, "aplicacion/ciudad_alojamientos.html", contexto)

@login_required  # Esta función la cree para poder agregar más opciones de ciudades
def nueva_ciudad(request):
    if request.method == "POST":
        miForm = CiudadForm(request.POST)
        if miForm.is_valid():
            city = miForm.cleaned_data.get("nombre")
            image = miForm.cleaned_data.get("imagen")
            ciudad = Ciudad(nombre=city, imagen=image)
            ciudad.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = CiudadForm()
    return render(request, "aplicacion/nueva_ciudad.html", {"form": miForm})

#______________________________________________________ Sobre mi
def about_me(request):
    return render(request, 'aplicacion/aboutMe.html')
from email.mime import image
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from AppCoder.models import Profesion
from AppCoder.forms import ProfesionFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario

#importaciones para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")
    


# Vistas de Mascota

def mascota(request):
    return render(request, "AppCoder/acerca_de_mi.html")

# Vistas de Profesiones

def profesion(request):
    profesion = Profesion.objects.all()
    contexto = {"profesion": profesion}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/foro.html", contexto)


def eliminar_profesion(request, id):
    profesion = Profesion.objects.get(id=id)
    borrado_id = profesion.id
    profesion.delete()
    url_final = f"{reverse('foro')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_profesion(request):
    if request.method == 'POST':
        formulario = ProfesionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesion = Profesion(nombre=data['nombre'])
            profesion.save()
            return redirect(reverse('foro'))
    else:  # GET
        formulario = ProfesionFormulario()
    return render(request, "AppCoder/form_profesion.html", {"formulario": formulario})


def editar_profesion(request, id):
    profesion = Profesion.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProfesionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            profesion.nombre = data['nombre']

            profesion.save()

            return redirect(reverse('foro'))
    else:  # GET
        inicial = {
            'nombre': profesion.nombre
        }
        formulario = ProfesionFormulario(initial=inicial)
    return render(request, "AppCoder/form_profesion.html", {"formulario": formulario})


# Vistas de Familiares

def familiar(request):
    return render(request, "AppCoder/blog.html")

#vista usuario

class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'AppCoder/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


#vista registro

def agregar_avatar(request):
    
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid:
            user = User.objects.get(username=request.user)
            avatar = form.save()
            avatar.user = user
            
            avatar.save()
            
            return redirect(reverse('inicio'))

    form = AvatarFormulario()
    return render(request, "AppCoder/form_avatar.html", {"form":form})

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html" , {"mensaje":"Usuario creado :D "})



    else:

        form = UserRegisterForm()

    
    return render(request, "AppCoder/registro.html" , {"form":form})


def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"AppCoder/login.html", {'form':form} )

class CustomLogoutView(LogoutView):
    template_name = 'AppCoder/logout.html'
    next_page = reverse_lazy('inicio')



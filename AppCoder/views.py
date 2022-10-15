from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from AppCoder.models import *
from AppCoder.forms import ProfesionFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario, PostForm

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
    return render(request, "AppCoder/index.html")

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
            
            miFormulario = AvatarFormulario(request.POST ,request.FILES)


            if miFormulario.is_valid:   


                u = User.objects.get(username=request.user)
                
                avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                avatar.save()

                return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= AvatarFormulario()

      return render(request, "AppCoder/form_avatar.html", {"miFormulario":miFormulario})


def urlImagen():

      return "/media/avatares/logo.jpg"

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



# Vista BLog

def insertPost(request):
    posts = Post.objects.all()
    posts = Post.objects.filter(state=True)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('/')    
    context = {'form':form,'posts':posts}
    return render (request, 'index.html',context)

def post(request, pk):
	post = Post.objects.get(id=pk)
	context = {'post':post}
	return render(request, 'post.html', context)

def editPost(request, pk):
    post =  Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('/')    
    context = {'form':form}
    return render (request, 'index.html',context)

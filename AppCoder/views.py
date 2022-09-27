from typing import Dict

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from AppCoder.models import Mascota, Familiar, Profesion
from AppCoder.forms import MascotaFormulario, ProfesionFormulario


def inicio(request):

    return render(request, "AppCoder/inicio.html")


# Vistas de Mascota

def mascota(request):
    mascota = Mascota.objects.all()
    return render(request, "AppCoder/mascota.html", {'mascota': mascota})


def crear_mascota(request):
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre=data['nombre'], edad=data['edad'])
            mascota.save()
            return render(request, "AppCoder/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = MascotaFormulario()  
    return render(request, "AppCoder/form_mascota.html", {"formulario": formulario})


def busqueda_mascota(request):
    return render(request, "AppCoder/form_busqueda_mascota.html")


def buscar_mascota(request):
    if request.GET["edad"]:
        edad = request.GET["edad"]
        mascota = Mascota.objects.filter(edad__icontains=edad)
        return render(request, "AppCoder/mascota.html", {'mascota': mascota})
    else:
        return render(request, "AppCoder/mascota.html", {'mascota': []})


# Vistas de Profesiones

def profesion(request):
    profesion = Profesion.objects.all()
    contexto = {"profesion": profesion}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/profesiones.html", contexto)


def eliminar_profesion(request, id):
    profesion = Profesion.objects.get(id=id)
    borrado_id = profesion.id
    profesion.delete()
    url_final = f"{reverse('profesion')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_profesion(request):
    if request.method == 'POST':
        formulario = ProfesionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesion = Profesion(nombre=data['nombre'])
            profesion.save()
            return redirect(reverse('profesion'))
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

            return redirect(reverse('profesion'))
    else:  # GET
        inicial = {
            'nombre': profesion.nombre
        }
        formulario = ProfesionFormulario(initial=inicial)
    return render(request, "AppCoder/form_profesion.html", {"formulario": formulario})


# Vistas de Familiares

class FamiliarListView(ListView):
    model = Familiar
    template_name = 'AppCoder/familiar.html'


class FamiliarCreateView(CreateView):
    model = Familiar
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('familiar')


class FamiliarUpdateView(UpdateView):
    model = Familiar
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('familiar')

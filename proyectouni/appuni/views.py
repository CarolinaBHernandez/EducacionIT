from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Alumno
from .forms import FormularioAlumno
from . import forms

def index(request):
    alumnos = Alumno.objects.all()
    ctx = {'alumnos': alumnos}
    return render(request, 'appuni/index.html', ctx)

def alumno(request, pk):
    try:
        alumno = Alumno.objects.get(id=pk)
    except Alumno.DoesNotExist:
        raise Http404("El alumno no se encuentra en la base de datos.")
    
    ctx = {'alumno': alumno}
    return render(request, 'appuni/alumno.html', ctx)


def nuevo_alumno(request):
    if request.method == "POST":
        form = FormularioAlumno(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = FormularioAlumno()
    ctx = { "form": form }
    return render(request, "appuni/nuevo_alumno.html", ctx)

def actualizar_alumno(request, pk):
    alumno = Alumno.objects.get(id=pk)
    if request.method == "POST":
        form = FormularioAlumno(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = FormularioAlumno(instance=alumno)
    return render(request, 'appuni/actualizar_alumno.html', {'form': form})

def eliminar_alumno(request, pk):
    alumno = Alumno.objects.get(id=pk)
    alumno.delete()
    return HttpResponseRedirect(reverse("index"))



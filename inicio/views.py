from django.shortcuts import render, redirect
from inicio.models import Mascotas
from inicio.forms import CrearMascotaFormulario, BusquedaMascotaFormulario, ActualizarMascotaFormulario

from django.contrib.auth.decorators import login_required


def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def sobre_mi(request):
    
    return render(request, 'inicio/sobre_mi.html', {})

def mascota(request):
    
    formulario = BusquedaMascotaFormulario(request.GET)
    if formulario.is_valid():
        tipo_a_buscar = formulario.cleaned_data.get('tipo')
        listado_de_mascotas = Mascotas.objects.filter(tipo__icontains = tipo_a_buscar)

    return render(request, 'inicio/mascotas.html', {'listado_de_mascotas': listado_de_mascotas})

@login_required
def crear_mascota(request):
    if request.method == "POST":
        formulario = CrearMascotaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            tipo = info_limpia.get('tipo')
            raza = info_limpia.get('raza')
            descripcion = info_limpia.get('descripcion')
            fecha_nacimiento = info_limpia.get('fecha_nacimiento')
            
            mascota = Mascotas(tipo=tipo, raza=raza, descripcion=descripcion, fecha_nacimiento=fecha_nacimiento)
            mascota.save()
            
            return redirect ('mascotas')
        
    formulario = CrearMascotaFormulario()
    return render(request, 'inicio/crear_mascota.html', {'formulario': formulario})

@login_required
def eliminar_mascota(request, mascota_id):
    
    Mascota_a_eliminar = Mascotas.objects.get(id=mascota_id)
    Mascota_a_eliminar.delete()
    return redirect ("mascotas")

@login_required
def actualizar_mascota(request, mascota_id):
    mascota_a_actualizar = Mascotas.objects.get(id=mascota_id)
    
    if request.method == 'POST':
        formulario = ActualizarMascotaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            mascota_a_actualizar.tipo = info_nueva.get('tipo')
            mascota_a_actualizar.raza = info_nueva.get('raza')
            mascota_a_actualizar.descripcion = info_nueva.get('descripcion')
            mascota_a_actualizar.fecha_nacimiento = info_nueva.get('fecha_nacimiento')
            
            mascota_a_actualizar.save()
            return redirect('mascotas')
        else:
            return render(request, 'inicio/actualizar_mascota.html', {'formulario': formulario})
            
    formulario = ActualizarMascotaFormulario(initial={'tipo':mascota_a_actualizar.tipo, 'raza':mascota_a_actualizar.raza, 'descripcion': mascota_a_actualizar.descripcion, 'fecha_nacimiento': mascota_a_actualizar.fecha_nacimiento})
    return render (request, 'inicio/actualizar_mascota.html', {'formulario':formulario})

def detalle_mascota(request, mascota_id):
    mascota = Mascotas.objects.get(id=mascota_id)
    
    return render (request, 'inicio/detalle_mascota.html', {'mascota': mascota})
from django.shortcuts import render, redirect
from inicio.models import Mascotas
from inicio.forms import CrearMascotasFormulario, BusquedaMascotasFormulario ,ActualizarMascotasFormulario
from django.contrib.auth.decorators import login_required


def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def sobre_mi(request):
    
    return render(request, 'inicio/sobre_mi.html', {})

def mascotas(request):
    formulario = BusquedaMascotasFormulario(request.GET)
    if formulario.is_valis():
        tipo_a_buscar = formulario.cleaned_data.get('tipo')
        listado_de_mascotas = Mascotas.objects.filter(raza__icontains=tipo_a_buscar)
        
    return render(request, 'inicio/mascotas.html', {'listado_de_mascotas': listado_de_mascotas})

@login_required
def crear_mascotas(request):
    if request.method == "POST":
        formulario = CrearMascotasFormulario(request.POST)
        info_limpia = formulario.cleaned_data
        
        tipo = info_limpia.get('tipo')
        raza = info_limpia.get('raza')
        descripcion = info_limpia.get('descripcion')
        fecha_nacimiento = info_limpia.get('fecha_nacimiento')
        
        mascota = mascota(tipo=tipo, raza=raza, descripcion=descripcion, fecha_nacimiento=fecha_nacimiento)
        mmascota.save()
        
        return redirect('mas')
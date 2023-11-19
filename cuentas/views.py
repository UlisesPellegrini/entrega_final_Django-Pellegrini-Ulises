from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from cuentas.forms import MiFormularioDeCreacion, EdicionPerfil
from cuentas.models import DatosExtras


def login (request):
    formulario = AuthenticationForm
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
        
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)

            DatosExtras.objects.get_or_create(user=request.user)

            return redirect('inicio')
    
    return render (request, 'cuentas/login.html', {'formulario_de_login': formulario})

def registro(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
    
    return render (request, 'cuentas/registro.html', {'formulario_de_registro': MiFormularioDeCreacion})

def editar_perfil(request):
    
    datos_extras = request.user.datosextras
    
    formulario = EdicionPerfil( instance=request.user, initial={'biografia': datos_extras.biografia, 'avatar': datos_extras.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extras.biografia = nueva_biografia
                
            if nuevo_avatar:
                datos_extras.avatar = nuevo_avatar
                
            datos_extras.save()
            formulario.save()
            
            return redirect('editar_perfil')
        
    return render (request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')
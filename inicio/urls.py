from django.urls import path
from inicio.views import inicio, sobre_mi, mascota, crear_mascota, detalle_mascota, eliminar_mascota, actualizar_mascota

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre_mi', sobre_mi, name='sobre_mi'),
    
    path('mascotas/', mascota, name='mascotas'),
    
    path ('mascotas/crear/', crear_mascota, name='crear_mascota'),
    
    path ('mascotas/<int:mascota_id>/detalle/', detalle_mascota, name='detalle_mascota'),
    path ('mascotas/<int:mascota_id>/eliminar/', eliminar_mascota, name='eliminar_mascota'),
    path ('mascotas/<int:mascota_id>/actualizar/', actualizar_mascota, name='actualizar_mascota'),
]
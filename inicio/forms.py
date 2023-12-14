from django import forms
from ckeditor.fields import RichTextFormField

class BaseMascotaFormulario(forms.Form):
    tipo = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    descripcion = RichTextFormField()
    fecha_nacimiento = forms.DateField()
    
class CrearMascotaFormulario(BaseMascotaFormulario):
    ...

class BusquedaMascotaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)
    
class ActualizarMascotaFormulario(BaseMascotaFormulario):
    ...
from django import forms
from ckeditor.fields import RichTextFormField

class BaseMascotasFormulario(forms.Form):
    tipo = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    descripcion = RichTextFormField()
    fecha_nacimiento = models.DateField()
    
class CrearMascotasFormulario(BasePaletasFormulario):
    ...

class BusquedaMascotasFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class ActualizarMascotasFormulario(BasePaletasFormulario):
    ...
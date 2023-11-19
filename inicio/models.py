from django.db import models
from ckeditor.fields import RichTextField

class Mascotas(models.Model):
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f'{self.raza} - {self.tipo}'
    

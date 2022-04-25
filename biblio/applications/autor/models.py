from django.db import models
# Managers
from .managers import AutorManager 

class Persona(models.Model):
    nombres = models.CharField(max_length=50) 
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    class Meta:
        abstract = True  # NO SE CREA EL MODELO PERSONA PERO LOS QUE HEREDAN DE ESTE MODELO SI APARECE LA INFO EN EL ADMIN
        
    def __str__(self):
        return self.nombres + ' ' + self.apellidos


class Autor(Persona):
    seudonimo = models.CharField('Seudonimo', max_length=50, blank=True)
    objects = AutorManager() 

    
    
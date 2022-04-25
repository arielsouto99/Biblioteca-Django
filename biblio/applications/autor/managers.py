from django.db import models
from django.db. models import Q

class AutorManager(models.Manager):
    # Managers para el modelo autor # 

 #! CONSULTAS BASICAS
    # Listar autores
    def listar_autores(self):
        return self.all()

    # Buscar autor por filtrado 1 (nombre)
    def buscar_autor(self,kword):
        resultado = self.filter(
            nombres__icontains=kword
        )
        return resultado

    # Buscar autor por filtrado 2 (nombre o apellido)
    def buscar_autor2(self,kword):
        resultado = self.filter(
            Q(nombres__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    # Buscar autor por filtrado 3 (nombre o apellido excluyendo edades = 35 o 52)
    def buscar_autor3(self,kword):
        resultado = self.filter(
            nombres__icontains=kword
        ).exclude(
            Q(edad__icontains=35) | Q(edad__icontains=52)
        )
        return resultado

    # Buscar autor por filtrado 4 (edades mayores que 40 y menores que 70)
    def buscar_autor4(self,kword):
        resultado = self.filter(
            edad__gt = 40,
            edad__lt = 70
        ).order_by('nombres')
        return resultado




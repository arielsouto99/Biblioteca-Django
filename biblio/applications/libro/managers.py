import datetime
from django.db import models
from django.db. models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity

#! CONSULTAS BASICAS
class LibroManager(models.Manager):
    # Managers para el modelo libro # 

    # Listar libros
    def listar_libros(self,kword):
        resultado = self.filter(
            titulo__icontains=kword,
        )
        return resultado

    # Consulta por fecha
    def fecha_libros(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return resultado

    # Anadir autor ya existente a un libro en ManyToMany
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro


#! TRIAGRAM 
    def listar_libros_trg(self,kword):
        
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,
            )
            return resultado
        else:
            return self.all()[:10] #Que me muestre los primeros 10


#! CONSULTAS FOREIGN KEY
    
    # Lista categorias
    def listar_libros_categorias(self, categoria):
        return self.filter(
            categoria__id=categoria #Puede ser el nombre pero el id es unico en todos los modelos
        ).order_by('titulo')

    # Veces que se presto un libro
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )
        return resultado

    # Veces que se presto un libro 2
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados = Count('libro_prestamo')
        )

        for r in resultado:
            print('********')
            print(r, r.num_prestados)

class CategoriaManager(models.Manager):
    # Managers para el modelo categoria # 

    # Filtrar categorias por autor (a que categoria pertenece el autor)
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    # Mostrar cuantos libros hay en una categoria
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
        return resultado

    
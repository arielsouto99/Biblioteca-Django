from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Models local
from .models import Libro

class ListLibros(ListView):
    model = Libro
    context_object_name = "list_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        # fecha1
        f1 = self.request.GET.get("fecha1", '')
        # fecha2
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Libro.objects.fecha_libros(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrg(ListView):
    model = Libro
    context_object_name = "list_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
       
        return Libro.objects.listar_libros_trg(palabra_clave)

class ListLibrosCategory(ListView):
    model = Libro
    context_object_name = "list_libros_categoria"
    template_name = "libro/lista_categoria.html"

    def get_queryset(self):
        return Libro.objects.listar_libros_categorias('1')
    
class LibroDetailView(DetailView):
    model = Libro
    context_object_name='libro'
    template_name = "libro/detalle.html"



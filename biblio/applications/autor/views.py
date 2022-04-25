from django.shortcuts import render
from django.views.generic import ListView
# Models local
from .models import Autor

class ListAutores(ListView):
    model = Autor
    context_object_name = "list_autores"
    template_name = "autor/lista.html"

    # # Listar autores
    # def get_queryset(self):
    #     return Autor.objects.listar_autores()

    # # Buscar autor por filtrado 
    # def get_queryset(self):
    #     palabra_clave = self.request.GET.get("kword", '')

    #     return Autor.objects.buscar_autor(palabra_clave)

    # Buscar autor por filtrado 2
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Autor.objects.buscar_autor2(palabra_clave)
    
    # Buscar autor por filtrado 3 
    # def get_queryset(self):
    #     palabra_clave = self.request.GET.get("kword", '')

    #     return Autor.objects.buscar_autor3(palabra_clave)
    
    # # Buscar autor por filtrado 4
    # def get_queryset(self):
    #     palabra_clave = self.request.GET.get("kword", '')

    #     return Autor.objects.buscar_autor4(palabra_clave)
    

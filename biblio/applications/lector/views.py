from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from applications.libro.models import Libro
from .models import Prestamo
from .forms import PrestamoForm, MultiPrestamoForm 

class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        
    #! Metodo create directamente con la orm de django
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # )

    #! Metodo save indirectamente con la orm de djano
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()

    # Descontando Stock de libros una vez prestados desde una url
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)


class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        
        # Si no existe lo registramos y si existe recuperamos el objeto
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                'fecha_prestamo' : date.today()
            }

        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
    
class AddMultiPrestamo(FormView):
    template_name = 'lector/add_multiprestamo.html'
    form_class = MultiPrestamoForm
    success_url = '.'

    def form_valid(self, form):
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False
            )
            prestamos.append(prestamo)
        
        libros = []
        for l in prestamos:
            l.libro.stock -= 1
            libros.append(l.libro)
 
        Libro.objects.bulk_update(
            libros,
            ['stock'],
        )
        
        Prestamo.objects.bulk_create(prestamos)

        return super(AddMultiPrestamo, self).form_valid(form)
             
from django.db import models
from django.db.models.signals import post_save

# Pillow app terceros
from PIL import Image

from .signals import optimize_image
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    objects = CategoriaManager()
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']

    def __str__(self):
        return str(self.id) + '-' + self.titulo

def optimize_image(sender, instance, **kwargs):

    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

# Conexion del signal save
post_save.connect(optimize_image, sender=Libro)
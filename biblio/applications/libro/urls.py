from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-trg/', views.ListLibrosTrg.as_view(), name='libros-trg'),
    path('libros-categoria/', views.ListLibrosCategory.as_view(), name='categoria'),
    path('libros-detalle/<pk>/', views.LibroDetailView.as_view(), name='detalle'),
]

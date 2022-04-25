# Generated by Django 4.0.1 on 2022-04-21 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField(verbose_name='Fecha de lanzamiento')),
                ('portada', models.ImageField(blank=True, upload_to='portada')),
                ('visitas', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='libro.categoria')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo', 'fecha'],
            },
        ),
    ]

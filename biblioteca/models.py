from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self): # __unicode__ en Python 2
        return self.nombre
    class Meta:
        ordering = ["nombre"]

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self): # __unicode__ en Python 2
       return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor,on_delete=models.SET_NULL,null=True)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas')
    def __str__(self): # __unicode__ en Python 2
        return self.titulo
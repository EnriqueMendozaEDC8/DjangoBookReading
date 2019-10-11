from django.contrib import admin
from biblioteca.models import Editor, Autor, Libro
# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')
    search_fields = ('nombre', 'apellidos')#filtrado por busqueda por campo

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_publicacion')#despliegue en tabla
    list_filter = ('fecha_publicacion',)#filtrado de busqueda en lista
    date_hierarchy = 'fecha_publicacion'
    fields = ('titulo','portada', 'autores', 'editor', 'fecha_publicacion') #Ordenar la ventana de edicion
    filter_horizontal = ('autores',) #filter_vertical
    raw_id_fields = ('editor',) # realizar una busqueda

admin.site.register(Editor)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
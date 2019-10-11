from django.shortcuts import render
from django.http import HttpResponse

from biblioteca.models import Libro
# Create your views here.
def formulario_buscar(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'resultados.html', {'libros': libros, 'query': q})
    return render(request, 'formulario_buscar.html', {'error': error})

def buscar(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un término de búsqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un término de búsqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'resultados.html',{'libros': libros, 'query': q})
    return render(request, 'formulario_buscar.html',{'error': errors})
    #return HttpResponse(mensaje)
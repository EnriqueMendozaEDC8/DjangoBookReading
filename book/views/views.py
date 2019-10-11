from django.http import HttpResponse,HttpRequest
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime
def hola(request):
    return HttpResponse("Hola mundo")

def vista_actual_url(request):
    return HttpResponse("bienvenido a mi pagina en %s" % request.path)
    
def fecha_actual(request):
    ahora = datetime.datetime.now()
    #t = Template("<html><body><h1>Fecha:</h1><h3>{{fecha_actual}}<h/3></body></html>")
    """ t = get_template('fecha_actual.html')
    html = t.render(Context(
        {
            'fecha_actual':ahora
        }
    ))
    return HttpResponse(html) """
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

def fecha_antes(request):
    html = ""
    try:
        if request.method == 'GET':
            #print(request.GET['value'])
            dt= datetime.datetime.now()+datetime.timedelta(hours=int(request.GET['value']))
            #html = "<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
            parameters = {
                'hora_siguiente': dt,
                'horas': int(request.GET['value']) 
            }
            return render(request, 'horas_adelante.html', parameters)
    except:
        html="ha ocurrido un error"
    return HttpResponse(html)
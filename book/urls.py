"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views.views import hola,fecha_actual,fecha_antes,vista_actual_url
from biblioteca.views import formulario_buscar,buscar
from contactos.views import contactos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola),
    path('fecha/', fecha_actual),
    path('fechaantes/', fecha_antes),
    path('actualurl/', vista_actual_url),
    path('formulario­buscar/', formulario_buscar),
    path('buscar/', buscar),
    path('contactos/', contactos),
]

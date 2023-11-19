from django.shortcuts import render
from django.http import HttpResponse

from .models import Sucursales
from .models import Doctores

# Create your views here.

def index(request):
    return render(request,"index.html")

def departamentos(request):
    return render(request,"departamentos.html")

def doctores(request):
    data = Doctores.objects.all()
    info = {
        "Doctores" : data
    }
    return render(request,"doctores.html",  context=info)

def sucursales(request):
    data = Sucursales.objects.all()
    info = {
        "Sucursales" : data
    }
    return render(request,"sucursales.html",  context=info)

def servicios(request):
    return render(request,"servicios.html")
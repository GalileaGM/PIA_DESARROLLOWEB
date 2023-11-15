from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return render(request,"index.html")

def departamentos(request):
    return render(request,"departamentos.html")

def doctores(request):
    return render(request,"doctores.html")

def sucursales(request):
    return render(request,"sucursales.html")

def servicios(request):
    return render(request,"servicios.html")
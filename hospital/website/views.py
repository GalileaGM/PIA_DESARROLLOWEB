from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return render(request,"index.html")

def departamentos(request):
    return render(request,"departamentos.html")

def medicos(request):
    return render(request,"medicos.html")

def sucursales(request):
    return render(request,"sucursales.html")

def ambulancias(request):
    return render(request,"ambulancias.html")
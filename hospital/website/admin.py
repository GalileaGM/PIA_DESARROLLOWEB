from django.contrib import admin
from django.urls import include, path

from .models import Doctores
from .models import Sucursales

# Register your models here.
admin.site.register(Doctores)
admin.site.register(Sucursales)
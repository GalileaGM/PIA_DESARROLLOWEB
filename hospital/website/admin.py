from django.contrib import admin
from django.urls import include, path

from .models import Doctor
from .models import Sucursales

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Sucursales)
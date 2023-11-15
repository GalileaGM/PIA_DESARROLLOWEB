from django.contrib import admin
from django.urls import include, path

from .models import Doctor

# Register your models here.
admin.site.register(Doctor)
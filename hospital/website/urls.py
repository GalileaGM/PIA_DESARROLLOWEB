from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('departamentos/', views.departamentos, name="departamentos"),
    path('doctores/', views.doctores, name="doctores"),
    path('sucursales/', views.sucursales, name="sucursales"),
    path('servicios/', views.servicios, name="servicios")
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('departamentos/', views.departamentos, name="departamentos"),
    path('medicos/', views.medicos, name="medicos"),
    path('sucursales/', views.sucursales, name="sucursales"),
    path('ambulancias/', views.ambulancias, name="ambulancias")
]
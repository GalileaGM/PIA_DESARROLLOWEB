from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre =models.CharField(max_length=60) #caracter
    direccion= models.CharField(max_length=50)
    peso= models.FloatField()#numero
    edad= models.IntegerField()
    fechacumple= models.DateTimeField()

    def __str__(self):#es para cambiar el nombre y que aparezca en la pantalla
        return self.nombre

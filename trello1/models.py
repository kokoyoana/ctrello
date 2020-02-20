from django.db import models

# Create your models here.
class Tablero(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Tablero")
    
    def __str__(self):
        fktab = self.nombre
        return fktab

class Lista(models.Model):
    nombreLista = models.CharField(max_length=50)
    fkTablero = models.ForeignKey(Tablero,on_delete=models.CASCADE, related_name="listas")
    
    def __str__(self):
        NombreLis = self.nombreLista 
        return NombreLis

class Tarea(models.Model):
    nombreTare = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fkLista = models.ForeignKey(Lista,on_delete=models.CASCADE, related_name="tareas")
    #test


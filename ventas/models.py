from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    def __str__(self):
        return f'Mi nombre es {self.nombre}'

class Ventas(models.Model):
    producto=models.CharField(max_length=50)

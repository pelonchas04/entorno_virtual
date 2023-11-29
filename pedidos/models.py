from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_completo=models.CharField(max_length=50)
    dpi=models.IntegerField()
    nit=models.IntegerField()
    telefono=models.CharField(max_length=14)
    email=models.EmailField()

class Proveedor(models.Model):
    nombre_pro=models.CharField(max_length=30)
    codgio_pro=models.IntegerField()
    
class Articulo(models.Model):
    articulo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    precio_venta=models.IntegerField()
    precio_compra=models.IntegerField()
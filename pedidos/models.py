from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_completo=models.CharField(max_length=50, verbose_name="Nombre")
    dpi=models.IntegerField()
    nit=models.IntegerField()
    telefono=models.CharField(max_length=14)
    email=models.EmailField(blank=True, null=True)
    # fecha_registro=models.BooleanField()
    def __str__(self):
        return f"Hola, me llamo {self.nombre_completo}"

class Proveedor(models.Model):
    nombre_pro=models.CharField(max_length=30)
    codgio_pro=models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre_pro}"
    
class Articulo(models.Model):
    articulo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    precio_venta=models.IntegerField()
    precio_compra=models.IntegerField()
    def __str__(self):
        return f"Articulo: {self.articulo} {self.marca} {self.modelo}"
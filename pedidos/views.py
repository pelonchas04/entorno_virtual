from django.shortcuts import render
from django.http import HttpResponse


def Busqueda_productos(request):

    return (render(request, "busqueda_productos.html"))

def Buscar(request):

    mensaje = f"Articulo Buscado: {request.GET['Busqueda']}"

    return HttpResponse(mensaje)
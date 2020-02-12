from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
import datetime


def HolaMundos(request):
   return HttpResponse("Hola Mundos")

def ejemHtml(request):
    documento = open("C:/Users/formacion/Documents/2020/proyectosdjango/proyecto1/proyecto1/plantillas/index.html")
    nombre = "Ernesto"
    edad = " 32"
    plantilla = Template(documento.read())
    documento.close()
    contexto1 = Context({"nomb":nombre,"edad":edad})
    doc = plantilla.render(contexto1)
    return HttpResponse(doc)

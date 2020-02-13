from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
import datetime


def ver(request):
   return HttpResponse("Vamos a ver")

def ejemHtml(request):
    documento = open("C:/Users/formacion/Documents/GitHub/ctrello/trello1/template/trello1/testvista.html")
    nombre = "Prueba"
    edad = " 100"
    plantilla = Template(documento.read())
    documento.close()
    contexto1 = Context({"nomb":nombre,"edad":edad})
    doc = plantilla.render(contexto1)
    return HttpResponse(doc)

from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render

def tres(request):
    nombre="dayana"
    edad="100"
    documento = open("C:/Users/formacion/Documents/GitHub/ctrello/trello1/template/trello1/indextrello.html")

    plantilla = Template(documento.read())
    documento.close()
    contexto =Context({"nomb":nombre, "ed":edad})
    doc = plantilla.render(contexto)
    return HttpResponse(doc)
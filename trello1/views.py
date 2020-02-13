from django.shortcuts import render
from django.forms import ModelForm
from trello1.models import Tablero,Lista,Tarea

class TableroForm(ModelForm):
    class Meta:
        model= Tablero
        fields= ['nombre',]
        
class ListaForm(ModelForm):
    class Meta:
        model= Lista
        fields= ['nombreLista','fkTablero',]
        
class TareaForm(ModelForm):
    class Meta:
        model= Tarea
        fields= ['nombreTare','descripcion','fkLista']

def index(request):
    principal = "trello1/index.html"
    formTablero = TableroForm(request.POST or None)
    if formTablero.is_valid():
        formTablero.save()
    return render(request,principal, {'formTablero':formTablero})

def fl(request):
    principal = "trello1/fl.html"
    formLista = ListaForm(request.POST or None)
    if formLista.is_valid():
        formLista.save()
    return render(request,principal, {'formLista':formLista})

def ft(request):
    principal = "trello1/ft.html"
    formTarea = TareaForm(request.POST or None)
    if formTarea.is_valid():
        formTarea.save()
    return render(request,principal, {'formTarea':formTarea})

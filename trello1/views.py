from django.shortcuts import render,redirect,get_object_or_404
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

def formlista(request):
    principal = "trello1/fl.html"
    formLista = ListaForm(request.POST or None)
    if formLista.is_valid():
        formLista.save()
    return render(request,principal, {'formLista':formLista})

def formtarea(request):
    principal = "trello1/ft.html"
    formTarea = TareaForm(request.POST or None)
    if formTarea.is_valid():
        formTarea.save()
    return render(request,principal, {'formTarea':formTarea})

def consultarTarea(request):
    template='trello1/consultarTarea.html'
    listatarea=Tarea.objects.all()
    contexto={}
    contexto['object_list']=listatarea
    return render (request,template,contexto)


def consultarTablero(request):
    template='trello1/consultarTablero.html'
    listatablero=Tablero.objects.all()
    contexto={}
    contexto['object_list']=listatablero
    return render (request,template,contexto)

def consultarLista(request):
    template='trello1/consultarLista.html'
    listas=Lista.objects.all()
    contexto={}
    contexto['object_list']=listas
    return render (request,template,contexto)

''''def update_tablero(request,id):
    template= 'trello1/edit.html'
    info_tablero=get_object_or_404(Tablero,pk=id)
    form = TableroForm(request.POST or None,instance=info_tablero)
    if form.is_valid():
        form.save()
        return redirect('trello1/consultarTablero.html')
        return render (request,template,{'form':form})'''

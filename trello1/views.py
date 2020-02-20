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
    return render(request,'trello1/index.html', {})

def formtablero(request):
    principal = "trello1/crearTablero.html"
    formTablero = TableroForm(request.POST or None)
    if formTablero.is_valid():
        formTablero.save()
    return render(request,principal, {'formTablero':formTablero})

def formlista(request):
    principal = "trello1/crearLista.html"
    formLista = ListaForm(request.POST or None)
    if formLista.is_valid():
        formLista.save()
    return render(request,principal, {'formLista':formLista})

def formtarea(request):
    principal = "trello1/crearTarea.html"
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
    listatablero= Tablero.objects.all()  
    contexto={}
    contexto['object_list']=listatablero
    return render (request,template,contexto)

def consultargeneral(request,id):
    template='trello1/tablerogeneral.html'
    tableros = Tablero.objects.prefetch_related('listas__tareas')
    tablero = get_object_or_404(tableros,pk=id)
    return render (request,template,{'tablero':tablero})

def consultarLista(request):
    template='trello1/consultarLista.html'
    listas= Lista.objects.all()  
    contexto={}
    contexto['object_list']=listas
    return render (request,template,contexto)

def update_tablero(request,id):
    template= 'trello1/editarTablero.html'
    info_tablero=get_object_or_404(Tablero,pk=id)
    form = TableroForm(request.POST or None,instance=info_tablero)
    if form.is_valid():
        form.save()
        return redirect('consultarTablero')
    return render (request,template,{'form':form})

def update_tarea(request,id):
    template= 'trello1/editarTarea.html'
    info_tarea=get_object_or_404(Tarea,pk=id)
    form = TareaForm(request.POST or None,instance=info_tarea)
    if form.is_valid():
        form.save()
        return redirect('consultarTarea')
    return render (request,template,{'form':form})
    
    
def update_lista(request,id):
    template= 'trello1/editarLista.html'
    info_lista=get_object_or_404(Lista,pk=id)
    form = ListaForm(request.POST or None,instance=info_lista)
    if form.is_valid():
        form.save()
        return redirect('consultarLista')
    return render (request,template,{'form':form})


def eliminar_tablero(request,id):
    template= 'trello1/confirmarEliminar.html'
    idTablero=get_object_or_404(Tablero,pk=id)
    if request.method == 'POST':
        idTablero.delete()
        return redirect('consultarTablero')
    return render (request,template,{'cli':idTablero})

def eliminar_tarea(request,id):
    template= 'trello1/confirmarEliminar.html'
    idTarea=get_object_or_404(Tarea,pk=id)
    if request.method == 'POST':
        idTarea.delete()
        return redirect('consultarTarea.html')
    return render (request,template,{'cli':idTarea})

def eliminar_lista(request,id):
    template= 'trello1/confirmarEliminar.html'
    idLista=get_object_or_404(Lista,pk=id)
    if request.method == 'POST':
        idLista.delete()
        return redirect('consultarLista.html')
    return render (request,template,{'cli':idLista})




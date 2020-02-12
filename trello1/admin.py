from django.contrib import admin
from .models import *
# Register your models here.
class TableroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class ListaAdmin(admin.ModelAdmin):
    list_display = ('nombreLista','fkTablero')



class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombreTare','descripcion','fkLista')


admin.site.register(Tablero,TableroAdmin)
admin.site.register(Lista,ListaAdmin)
admin.site.register(Tarea,TareaAdmin)

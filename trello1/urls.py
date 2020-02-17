from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.formlista, name='formlista'),
    path('tarea', views.formtarea, name='formtarea'),
    path('consultarTarea', views.consultarTarea, name='consultarTarea'),
    path('consultarTablero', views.consultarTablero, name='consultarTablero'),
    path('consultarLista', views.consultarLista, name='consultarLista'),
]
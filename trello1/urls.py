from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tablero', views.formtablero, name='formtablero'),
    path('lista', views.formlista, name='formlista'),
    path('tarea', views.formtarea, name='formtarea'),
    path('consultarTarea', views.consultarTarea, name='consultarTarea'),
    path('consultarTablero', views.consultarTablero, name='consultarTablero'),
    path('consultarLista', views.consultarLista, name='consultarLista'),
    path('modificarTablero/<int:id>', views.update_tablero, name='update_tablero'),
    path('modificarTarea/<int:id>', views.update_tarea, name='update_tarea'),
    path('modificarLista/<int:id>', views.update_lista, name='update_lista'),
    path('eliminarTablero/<int:id>',views.eliminar_tablero,name='eliminar_tablero' ),
    path('eliminarTarea/<int:id>',views.eliminar_tarea,name='eliminar_tarea' ),
    path('eliminarLista/<int:id>',views.eliminar_lista,name='eliminar_lista' ),
]
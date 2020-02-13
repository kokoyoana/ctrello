from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.formlista, name='formlista'),
    path('tarea', views.formtarea, name='formtarea'),
]
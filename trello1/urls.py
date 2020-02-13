from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.fl, name='fl'),
    path('tarea', views.ft, name='ft'),
]
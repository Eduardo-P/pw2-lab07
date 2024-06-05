from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agregar_destino/", views.destinationCreate, name="DestinationCreate"),
    path('agregar_destino/<int:myID>/', views.destinationEdit, name='DestinationEdit'),
    path('eliminar_destino/<int:myID>/', views.destinationDelete, name='DestinationDelete')
]

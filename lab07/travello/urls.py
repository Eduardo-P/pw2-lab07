from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agregar_destino", views.destinationCreate, name="DestinationCreate")
]

from django.db import models

# Create your models here.
class Destination:
    nombreCiudad: str
    descripcionCiudad: str
    imagenCiudad: str
    precioTour: int
    ofertaTour: bool
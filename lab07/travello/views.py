from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.nombreCiudad = 'Mumbai'
    dest1.descripcionCiudad = 'The City That Never Sleeps'
    dest1.imagenCiudad = 'destination_1.jpg'
    dest1.precioTour = 700
    
    dest2 = Destination()
    dest2.nombreCiudad = 'Hyderabad'
    dest2.descripcionCiudad = 'First Biryani, The Sherwani'
    dest2.imagenCiudad = 'destination_2.jpg'
    dest2.precioTour = 650
    
    dest3 = Destination()
    dest3.nombreCiudad = 'Bengaluru'
    dest3.descripcionCiudad = 'Beatutiful City'
    dest3.imagenCiudad = 'destination_3.jpg'
    dest3.precioTour = 750
    
    dests = {dest1, dest2, dest3}
    
    return render(request, "index.html", {'dests': dests})
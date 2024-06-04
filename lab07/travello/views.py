from django.shortcuts import render
from .models import Destination
from .forms import DestinationForm

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    
    return render(request, "index.html", {'dests': dests})

def destinationCreate(request):
    form = DestinationForm(request.POST or None)
    if form.id_valid():
        form.save()
        form = DestinationForm()
    
    context = {
        'form': form
    }
    return render(request, 'destinationCreate.html', context)
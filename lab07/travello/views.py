from django.shortcuts import render, get_object_or_404
from .models import Destination
from .forms import DestinationForm

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    
    return render(request, "index.html", {'dests': dests})

def destinationCreate(request):
    form = DestinationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DestinationForm()
    
    context = {
        'form': form
    }
    return render(request, 'destinationCreate.html', context)

def destinationEdit(request, myID):
    obj = get_object_or_404(Destination, id = myID)
    
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            form = DestinationForm()
    else:
        form = DestinationForm(instance = obj)
    
    context = {
        'form': form
    }
    return render(request, 'destinationCreate.html', context)

def destinationDelete(request, myID):
    obj = get_object_or_404(Destination, id = myID)
    if request.method == 'POST':
        obj.delete()
        
    context = {
        'objeto': obj
    }
    return render(request, 'destinationDelete.html', context)
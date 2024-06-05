from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    
    return render(request, "index.html", {'dests': dests})

def destinationCreate(request):
    form = DestinationForm(request.POST, request.FILES or None)
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
        if 'eliminar' in request.POST:
            obj.delete()
        elif 'cancelar' in request.POST:
            return redirect('../../')
        
    context = {
        'objeto': obj
    }
    return render(request, 'destinationDelete.html', context)

def destinationList(request):
    destinations = Destination.objects.all()
    
    context = {
        'objectList': destinations
    }
    return render(request, 'destinationList.html', context)
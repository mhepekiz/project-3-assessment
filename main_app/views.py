from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Wacky
# Create your views here.
def index(request):
    wackies = Wacky.objects.all()
    return render(request, 'index.html', {'wackies': wackies})

class WackyCreate(CreateView):
    model = Wacky
    fields = '__all__'


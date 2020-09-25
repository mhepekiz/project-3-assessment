from django.shortcuts import render, redirect
from .models import Wacky
from .forms import WackyForm

# Create your views here.


def index(request):
    wacky_list = Wacky.objects.all()
    wacky_form = WackyForm()
  
    return render(request, 'index.html', {'wacky_list': wacky_list, 'wacky_form': wacky_form,
    })

def add_wacky(request):
    form = WackyForm(request.POST)
    if form.is_valid():
        add_wacky = form.save()
    return redirect('/')


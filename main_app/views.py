from django.shortcuts import render, redirect
from .models import Wacky

# Create your views here.


def index(request):
    wacky_list = Wacky.objects.all()
  
    return render(request, 'index.html', {'wacky_list': wacky_list})


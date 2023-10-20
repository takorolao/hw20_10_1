from django.shortcuts import render
from .models import Flower, Bouquet

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flower_list.html', {'flowers': flowers})

def bouquet_list(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'bouquet_list.html', {'bouquets': bouquets})

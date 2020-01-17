from django.shortcuts import render
from .models import Lists
# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    items = Lists.objects.all
    context = {'lists': items}
    return render(request, 'home.html', context)

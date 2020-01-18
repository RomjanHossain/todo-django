from django.shortcuts import render, redirect
from .models import Lists
from .forms import ListForm
# Create your views here.


def base(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm()

    return render(request, 'base.html')


def home(request):
    items = Lists.objects.all
    return render(request, 'home.html', {'lists': items})

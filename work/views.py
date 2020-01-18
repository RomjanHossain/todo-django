from django.shortcuts import render, redirect
from .models import Lists
from .forms import ListForm
from django.contrib import messages
# Create your views here.


def base(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('home')
    else:
        form = ListForm()

    return render(request, 'base.html')


def home(request):
    items = Lists.objects.all
    return render(request, 'home.html', {'lists': items})


def delete(request, do_id):
    idd = Lists.objects.get(pk=do_id)
    idd.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('home')


def complete(request, id):
    idd = Lists.objects.get(pk=id)
    if idd.completed == True:
        idd.completed = False
        idd.save()
    else:
        idd.completed = True
        idd.save()
    return redirect('home')


def edit(request, id):
    if request.method == 'POST':
        idd = Lists.objects.get(pk=id)
        form = ListForm(request.POST, instance=idd)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task editted successfully!')
            return redirect('home')
    else:
        idd = Lists.objects.get(pk=id)
        return render(request, 'edit.html', {'idd': idd})

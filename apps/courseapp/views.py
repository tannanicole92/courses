from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'courseapp/index.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def destroy(request, id):
    delete_id = id
    context = {
        "id": Course.objects.get(id = delete_id),
    }
    return render(request, 'courseapp/destroy.html', context)

def delete(request, id):
    Course.objects.get(id = id).delete()
    return redirect('/')

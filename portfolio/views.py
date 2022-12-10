from django.shortcuts import render
from .models import *


def user(request):
    project = Project.objects.all()
    return render(request, 'home/home.html', {'projects': project})

def memes(request):
    project = Memes.objects.all()
    return render(request, 'blog/memes.html', {'projects': project})

from django.shortcuts import render
from .models import Sporty


def index(request):
    projects = Sporty.objects.all()
    return render(request, 'sporty/index.html', {'projects': projects})

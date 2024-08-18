from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def signupuser(request):
    if request.method == "GET":
        return render(request, 'registration/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('sporty/index.html')


def loginuser(request):
    return render(request, 'registration/loginuser.html', {'form': AuthenticationForm()})

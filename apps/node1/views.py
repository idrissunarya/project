from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
            return render (request, 'pages/dashboard.html')
    else:
        return render (request, 'pages/login.html')


def dashboard(request):
    return render (request, 'pages/dashboard.html')

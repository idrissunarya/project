from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib import messages

def web(request):
    return render (request, 'pages/web.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            return render(request, 'pages/dashboard.html')

        else:
            #return HttpResponse('failed login')
            messages.error(request,'username or password not correct')
            return render(request, 'pages/login.html')
    else:
        return render (request, 'pages/login.html')

def dashboard(request):
    return render (request, 'pages/dashboard.html')

from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            #return HttpResponse('success login')
            return render(request, 'pages/dashboard.html')

        else:
            #return HttpResponse('failed login')
            messages.error(request,'username or password not correct')
            return render(request, 'pages/login.html')
    else:
        return render (request, 'pages/login.html')


def dashboard(request):
    return render (request, 'pages/dashboard.html')

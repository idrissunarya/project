from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib import messages

def web(request):
    if request.method == 'GET':
        return render (request, 'pages/web.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user.is_authenticated:
            messages.success(request,'Improve your profile today!')
            return render(request, 'pages/dashboard.html')
            #return HttpResponse ('success')

        else:
            #return HttpResponse('failed login')
            messages.error(request,'username or password not correct')
            return render(request, 'pages/login.html')
    else:
            #messages.error(request, 'jangan by pass bos !!')
        return render (request, 'pages/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print(user)
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form' : form }
    return render (request, 'registration/register.html', context)

def logout(request):
    return render (request, 'registration/logout.html')

def dashboard(request):
   return render (request, 'pages/dashboard.html')

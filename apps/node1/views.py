from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from apps.node1.forms import SignUpForm, TestForm
from .models import Coba

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form })

#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)

#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password1']
#            user = authenticate(username=username, password=password)
#            print(user)
#            return redirect('login')

#    else:
#        form = UserCreationForm()

#    context = {'form' : form }
#    return render (request, 'registration/register.html', context)

def logout(request):
    return render (request, 'registration/logout.html')

def dashboard(request):
   return render (request, 'pages/dashboard.html')

def coba(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('subject')
            sender = form.cleaned_data.get('sender')

            send = authenticate(subject=subject, sender=sender)
            return redirect('dashboard')

    else:
        queryset = Coba.objects.all()
        context = {
            "q": queryset
        }
        form = TestForm()
    return render(request, 'pages/coba.html', {'form' : form }, context)

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.web, name='web'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('dashboard/', views.dashboard, name='dashboard'),
]
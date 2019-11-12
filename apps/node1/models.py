from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username

class Member(models.Model):
    GLOBAL = 'GIC'
    SATYA = 'SMG'
    COMPANY_IN_CHOICES = (
        (GLOBAL, 'Global inti Corporatama'),
        (SATYA, 'Satya Mitra Graha'),
    )

    DIRECTOR = 'DIR'
    MANAGER = 'MNG'
    SUPERVISOR = 'SUP'
    STAFF = 'STF'
    PROGRAMMER = 'PRO'
    ANDROID = 'AND'
    SYSTEM_ADM = 'SYS'
    NOC = 'NOC'
    HRD = 'HRD'
    FINANCE = 'FIN'
    SALES = 'SLS'
    TECHNICIAN = 'TEC'
    LOGISTIC = 'LOG'
    RECEPTIONIST = 'REC'
    OFFICEBOY = 'OBY'
    COURIER = 'CRI'
    DRIVER = 'DRI'
    DIVISI_IN_CHOICES = (
        (DIRECTOR, 'Director'),
        (MANAGER, 'Manager'),
        (SUPERVISOR, 'Supervisor'),
        (STAFF, 'Staff'),
        (PROGRAMMER, 'Programmer'),
        (ANDROID, 'Android Devloper'),
        (SYSTEM_ADM, 'System Administrator'),
        (NOC, 'Network Oprations Center'),
        (HRD, 'Human Resources Departement'),
        (FINANCE, 'Finance'),
        (SALES, 'Sales'),
        (TECHNICIAN, 'Technician'),
        (LOGISTIC, 'Logistic'),
        (RECEPTIONIST, 'Receptionist'),
        (OFFICEBOY, 'Office Boy'),
        (COURIER, 'Courier'),
        (DRIVER, 'Driver'),
    )

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    company = models.CharField(max_length=3,choices=COMPANY_IN_CHOICES,default=GLOBAL,)
    division = models.CharField(max_length=3,choices=DIVISI_IN_CHOICES,default=STAFF,)
    email = models.EmailField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.first_name


class Location(models.Model):
    address = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    postal = models.IntegerField()
    country = CountryField(blank_label='(select country)')

    class Meta:
        ordering = ['address']

    def __str__(self):
        return self.address

class Coba(models.Model):
    subject = models.CharField(max_length=64)
    sender = models.EmailField()
    compose = models.TextField(default='mail in here')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['sender']

    def __str__(self):
        return self.sender

class Product(models.Model):
    name = models.CharField(max_length=128)

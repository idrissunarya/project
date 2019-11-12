from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.node1.models import Coba

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=32, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=256, help_text='Required Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password1',)

class TestForm(forms.ModelForm):
    subject = forms.CharField(max_length=64)
    sender = forms.EmailField()

    class Meta:
        model = Coba
        fields = ('subject', 'sender', 'compose',)

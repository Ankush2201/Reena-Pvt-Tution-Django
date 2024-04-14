from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']

from django.contrib.auth import get_user_model


from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username: '}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name: '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email: '}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password: '}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password: '}),
            
        }


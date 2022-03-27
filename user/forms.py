from django import forms
from user.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
import time
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        min_length=4,
        label='Login', 
        widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Username"}
        )
    )
    phone = forms.CharField(
        label='Phone', 
        widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Phone"}
        )
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-input', "placeholder": "Email"}
        )
    )
    country = forms.CharField(
        label='Country', 
        widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Country"}
        )
    )
    password = forms.CharField(
        min_length=6, 
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder": "Passwword"}
        )
    )
    password2 = forms.CharField(
        label='Repeat password', 
        widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder": "Repeat password"}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'country', 'password', 'password2')

    def clean(self):
        super().clean()
        errors = {}
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            errors["password"] = ValidationError("Passwords don't match!!!!")
            raise ValidationError(errors)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Login', 
        widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder": "Password"}
        )
    )
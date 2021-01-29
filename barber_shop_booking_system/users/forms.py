from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_number', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_number', 'email']

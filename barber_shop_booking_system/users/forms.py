from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerInfo


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['mobile_number']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['mobile_number']

from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'login-input'

    # class Meta:
    #     model = User
    #     fields = ['email', 'password']
    #
    #     widgets = {
    #         'username': forms.TextInput(attrs={'placeholder': 'password', 'id': 'pswd'}),
    #     }

    class Meta:
        widgets = {
            'password': forms.TextInput(attrs={'class': 'input-class test-mtfker'})
        }

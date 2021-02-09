from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerInfo


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        for field in self.fields.values():
            field.label = ''
            field.help_text = None
            field.widget.attrs['class'] = 'login-input'

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }


class CustomerRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        self.fields['mobile_number'].label = ''

    class Meta:
        model = CustomerInfo
        fields = ['mobile_number']

        widgets = {
            'mobile_number': forms.TextInput(attrs={
                'class': 'login-input',
                'placeholder': 'Mobile Number',
                'label': None
            })
        }


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

    class Meta:
        fields = ['email', 'password']


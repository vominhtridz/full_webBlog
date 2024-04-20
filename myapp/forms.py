from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField()
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']  # Specify the fields from User model
        widgets = {
            'username': forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Nhập username...'}),
            'password1': forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Nhập mật khẩu...'}),
            'password2': forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Nhập lại mật khẩu...'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Nhập username...'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Nhập mật khẩu...'})
    )

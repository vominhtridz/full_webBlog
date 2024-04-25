from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']  # Specify the fields from User model
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'formInput', 'placeholder': 'Nhập username...'}),
            'password1': forms.PasswordInput(
                attrs={'class': 'formInput bg-[#eee] border-none my-8 px-[10px] py-[15px] text-[13px] rounded-[8px] w-full outline-none', 'placeholder': 'Nhập mật khẩu...'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'formInput bg-[#eee] border-none my-8 px-[10px] py-[15px] text-[13px] rounded-[8px] w-full outline-none', 'placeholder': 'Nhập lại mật khẩu...'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Nhập username...'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Nhập mật khẩu...'})
    )
# add post 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','topic', 'content', 'image', 'date', 'icon']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập tiêu đề ...'}),
        'topic': forms.Select(attrs={'class': 'border border-slate-500 px-2 py-1'}),
        'content': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập nội dung ...'}),
        'image': forms.FileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        'date': forms.DateInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập ngày ...'}),
        'icon': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập biểu tượng ...'}),
        }

     



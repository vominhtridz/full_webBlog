from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from .models import CommentChild
from .models import UserProfile


#form USER PROFILE

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'outline-blue-300 px-2 py-1.5 border border-gray-400 text-sm rounded-sm w-full', 'placeholder': 'Nhập email...'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'outline-blue-300 px-2 py-1.5 border border-gray-400 text-sm rounded-sm w-full', 'placeholder': 'Nhập địa chỉ...'}))
    day = forms.IntegerField(widget=forms.Select(attrs={'class': 'day border border-gray-400 rounded-sm px-3 py-1 mx-1'}))
    month = forms.IntegerField(widget=forms.Select(attrs={'class': 'month border border-gray-400 rounded-sm px-3 py-1 mx-1'}))
    year = forms.IntegerField(widget=forms.Select(attrs={'class': 'year border border-gray-400 rounded-sm px-3 py-1 mx-1'}))
    defaultName = forms.CharField(widget=forms.TextInput(attrs={'class': 'outline-blue-300 px-2 py-1.5 border border-gray-400 text-sm rounded-sm w-full', 'placeholder': 'Nhập tên...'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'px-2 py-1.5  text-sm rounded-sm w-full', 'placeholder': 'Nhập ...'}))
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'border border-gray-500 text-sm px-4 py-1.5'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'outline-blue-300 px-2 py-1.5 border border-gray-400 text-sm rounded-sm w-full', 'placeholder': 'Nhập số điện thoại...'}))
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'day', 'month', 'year', 'defaultName', 'email', 'image', 'gender']

# --------------------  SIGN UP FORM -------------------   
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
        
        
        
# -------------------------- LOGIN FORM --------------------------   

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Nhập username...'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Nhập mật khẩu...'})
    )
# -------------------------------------  POST FORM ---------------------------------   

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','topic', 'content', 'image']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập tiêu đề ...'}),
        'topic': forms.Select(attrs={'class': 'border border-slate-500 px-2 py-1'}),
        'content': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nhập nội dung ...'}),
        'image': forms.FileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        
        }
        
        
# -------------------------------------  COMMENT FATHER FORM ---------------------------------   

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
        widgets = {
            'comment_content': forms.TextInput(attrs={'class': 'px-4 py-2 rounded-sm outline-gray-400 border border-gray-500 ml-3 mr-6 text-sm w-full', 'placeholder': 'Nhập nội dung bình luận'}),
        }
        
# -------------------------------------  COMMENT CHILD FORM ---------------------------------   
    
class CommentChildForm(forms.ModelForm):
    class Meta:
        model = CommentChild
        fields = ['comment_content']
        widgets = {
            'comment_content': forms.TextInput(attrs={'class': 'px-2 py-1  text-[13px] rounded-sm outline-gray-400 border border-gray-500 ml-3 mr-6 text-sm w-full', 'placeholder': 'Nhập nội dung bình luận....','id': 'CMT_child'}),
        }
        

     



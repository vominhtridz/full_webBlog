
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from myapp.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from myapp.models import Image
from django.contrib.auth import logout
# Create your views here.
def home(request):
    user = request.user if request.user.is_authenticated else None
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images,'user': user})
def InforProduct(request):
    return render(request, 'inforProduct.html')
def Cart(request):
    return render(request, 'Cart.html')
def login(request):  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form': form, 'error_message': 'Username already exists.'})
            else:
                # Username is unique, save the form data
                form.save()
                return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
def nike(request):
    return render(request, 'nike.html')
def Adidas(request):
    return render(request, 'Adidas.html')
def Puma(request):
    return render(request, 'Puma.html')
def Asics(request):
    return render(request, 'Asics.html')
def Pelock(request):
    return render(request, 'Pelock.html')
def payment(request):
    return render(request, 'payment.html')

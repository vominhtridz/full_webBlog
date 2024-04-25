
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from myapp.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from myapp.models import Image
from django.contrib.auth import logout
from myapp.forms import PostForm
from myapp.models import Post
# Create your views here.
# home
def home(request):
    user = request.user if request.user.is_authenticated else None
    # ảnh banner trang home
    images = Image.objects.all() 
    # hiên tất cả bài blog
    posts = Post.objects.all()
    return render(request, 'home.html', {'images': images,'user': user,'posts': posts})
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Xóa bài post nếu yêu cầu là POST
        post.delete()
        return redirect('home')  # Hoặc chuyển hướng đến một trang khác
    # Nếu không phải yêu cầu POST, chuyển hướng đến trang chính
    return redirect('edit_post', post_id=post_id)
def updatePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of the view for your home page
    else:
        form = PostForm(instance=post)
    return render(request, 'update.html', {'form': form})
def Topic(request,post_id):
    
    post = Post.objects.get(id=post_id)
    relate_to = Post.objects.filter(topic=post.topic)
    return render(request, 'topic.html', {'post': post,'relate_to': relate_to})
def Category_page(request,category):
    category_item = Post.objects.filter(topic=category)
    category_topics = Post.objects.filter(topic=category).first()
    return render(request, 'Categories.html', {'category': category_item,'category_topics': category_topics})
# add post
def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Chuyển hướng về trang chủ sau khi lưu bài viết thành công
    else:
        form = PostForm()
    return render(request, 'AddPost.html', {'form': form})
# login
# 
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
# register

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
# logout
def user_logout(request):
    logout(request)
    return redirect('home')

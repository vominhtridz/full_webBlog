
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from myapp.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from myapp.models import Image
from django.contrib.auth import logout
from myapp.forms import PostForm
from myapp.models import Post
from myapp.models import Comment
from myapp.models import CommentChild
from myapp.models import UserProfile
from myapp.forms import CommentForm
from myapp.forms import CommentChildForm
from myapp.forms import UserProfileForm
import json
from django.contrib import messages


# Create your views here.
# home
def home(request):
    images = Image.objects.all() 
    user = request.user if request.user.is_authenticated else None
    # ảnh banner trang home
    current_user = request.user if request.user.is_authenticated else None
    # hiện tất cả bài blog
    posts = Post.objects.all()
    
    return render(request, 'home.html', {'images': images, 'user': user, 'posts': posts, 'current_user': current_user})
def SearchPage(request, search_value):
    PostsResult = Post.objects.filter(title= search_value)
    posts = Post.objects.all()
    return render(request, 'SearchPage.html', {'PostsResult': PostsResult,'posts':posts})
# blog của tôi 
def blog_ofMine(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    
    posts = Post.objects.filter(author= request.user)
    return render(request, 'blog_ofMine.html', {'posts': posts,'current_user':current_user})
#Profile
def Profile(request,user_id):
    if request.user.is_authenticated == False:
        return redirect('login')
   
    current_user = request.user if request.user.is_authenticated else None 
    form =   UserProfileForm(request.POST, request.FILES)
    posts = Post.objects.all()
    return render(request, 'Profile.html', {'posts': posts,'current_user':current_user,'form':form})
#save

def saveProfile(request,user_id):

    if request.user.is_authenticated == False:
        return redirect('login')
    Profile = get_object_or_404(UserProfile, id=user_id)
    form =   UserProfileForm(request.POST, request.FILES, instance= Profile)
    if form.is_valid():
        formDB = form.save(commit= False)
        formDB.id = user_id
        formDB.gender = request.POST.get('gender')
        formDB.save()
        messages.success(request, 'Lưu thông tin cá nhân thành công.')
        return redirect('home')
    messages.error(request, 'Kiểm tra lại các trường đã nhập đúng chưa.')
    return render(request, 'Profile.html',{'form':form})
    
            
        

# xoá bài blog 
def delete_post(request, post_id):
    if request.user.is_authenticated == False:
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Xóa bài post nếu yêu cầu là POST
        post.delete()
        return redirect('home')
        
def updatePost(request, post_id):
    if request.user.is_authenticated == False:
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all()
    current_user = request.user if request.user.is_authenticated else None
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of the view for your home page
    else:
        form = PostForm(instance=post, initial={'image': post.image})
    return render(request, 'update.html', {'form': form,'posts':posts,'current_user':current_user})

def Category_page(request,category):
    current_user = request.user if request.user.is_authenticated else None
    category_item = Post.objects.filter(topic=category)
    posts = Post.objects.all()
    category_topics = Post.objects.filter(topic=category).first()
    return render(request, 'Categories.html', {'current_user': current_user,'posts':posts, 'category': category_item,'category_topics': category_topics})
# add post
def AddPost(request):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Tạo một instance của bài viết nhưng chưa lưu vào database
            post.author = request.user  # Gán tác giả là username của người dùng hiện tại
             # Lưu bài viết vào database
            post.save()
            return redirect('home')  # Chuyển hướng về trang chủ sau khi lưu bài viết thành công
    else:
        form = PostForm()
    return render(request, 'AddPost.html', {'form': form,'current_user':current_user})
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
        
    posts = Post.objects.all()
    return render(request, 'login.html', {'form': form,'posts':posts})
# register

def register(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form': form,'posts':posts, 'error_message': 'Username already exists.'})
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
# topic
def Topic(request,post_id):
    posts = Post.objects.all()
    current_user = request.user if request.user.is_authenticated else None
    post = Post.objects.get(id=post_id)
    Post_Comment =Comment.objects.filter(topic_id=post_id) 
    comment_temp = CommentForm()
    #child
    Post_CommentChild =CommentChild.objects.filter(topic_id=post_id)
    commentChild_temp = CommentChildForm()
    relate_to = Post.objects.filter(topic=post.topic)
    return render(request, 'topic.html', 
    {'post': post,'relate_to': relate_to,'current_user':current_user, 'Post_CommentChild': Post_CommentChild, 
     'comment_temp':comment_temp,'Post_Comments':Post_Comment,'commentChild_temp':commentChild_temp,
     'posts':posts
     })
# Comment 
def Handle_Comment(request, post_id):
    current_user = request.user if request.user.is_authenticated else None
    if not request.user.is_authenticated:
        return redirect('login')
    # Lấy bài viết theo id  
    LengthCMTChild = len(Comment.objects.filter(topic_id=post_id))
    
    if request.method == 'POST':
        comment_temp = CommentForm(request.POST)
        if comment_temp.is_valid():
            comment_DB = comment_temp.save(commit=False)
            comment_DB.topic_id = post_id
            comment_DB.Commentid = LengthCMTChild
            comment_DB.comment_content = comment_temp.cleaned_data['comment_content']
            comment_DB.author = current_user
            comment_DB.save()
            return redirect('topic', post_id)
            
            
    else:
        return redirect('topic', post_id)
        
def Handle_CommentChild(request, post_id,comment_id):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    # Lấy bài viết theo id  
    comment_instant = Comment.objects.get(id = comment_id)
    comment_instant.reply_count += 1
    comment_instant.save(update_fields=['reply_count'])
    if request.method == 'POST':
        responder = request.POST.get('comment_author')
        comment_template = CommentChildForm(request.POST)
        if comment_template.is_valid():
            CommentChild_DB = comment_template.save(commit=False)
            CommentChild_DB.topic_id = post_id
            CommentChild_DB.tag = ''
            CommentChild_DB.comment_content = comment_template.cleaned_data['comment_content']
            CommentChild_DB.author = current_user
            CommentChild_DB.commentChild_id = comment_id
            CommentChild_DB.responder = responder
            CommentChild_DB.save()  
    return redirect('topic', post_id) 

def Handle_CommentTag(request, post_id,comment_id,comment_tag):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    # Lấy bài viết theo id  
    comment = Comment.objects.get(id = comment_id)
    comment.reply_count +=1
    comment.save(update_fields=['reply_count'])
    if request.method == 'POST':
        responder = request.POST.get('comment_author')
        comment_template = CommentChildForm(request.POST)
        if comment_template.is_valid():
            CommentChild_DB = comment_template.save(commit=False)
            CommentChild_DB.topic_id = post_id
            CommentChild_DB.tag = comment_tag
            CommentChild_DB.comment_content = comment_template.cleaned_data['comment_content']
            CommentChild_DB.author = current_user
            CommentChild_DB.commentChild_id = comment_id
            CommentChild_DB.responder = responder
            CommentChild_DB.save()  
    return redirect('topic', post_id)
    
def handleLike (request,post_id, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if(request.method == 'POST'):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.like += 1
        return JsonResponse({'success': True})
    else:
        comment = get_object_or_404(Comment, id=comment_id)
        comment.like -= 1
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
       
def handleLikeChild (request,post_id, comment_id):
    

    return redirect('topic', post_id)
       
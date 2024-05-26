
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from myapp.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from myapp.models import Image
from django.contrib.auth import logout
from myapp.forms import PostForm
from myapp.models import Post
from myapp.models import UserProfile
from myapp.models import Comment
from myapp.models import Notification

from myapp.models import CommentChild
from myapp.forms import CommentForm
from myapp.forms import CommentChildForm
from myapp.forms import UserProfileForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

import pytz
# Create your views here.
# -----------------handle Home Page-------------------
def home(request):
    images = Image.objects.all() 
    user = request.user if request.user.is_authenticated else None
    # ảnh banner trang home
    current_user = request.user if request.user.is_authenticated else None
    # hiện tất cả bài blog
    context = {'images': images, 'user': user, 'current_user': current_user}
    return render(request, 'home.html', context)
# -----------------handle search Page-------------------
def SearchPage(request, search_value):
    PostsResult = Post.objects.filter(title= search_value)
    context = {'PostsResult': PostsResult,}
    return render(request, 'SearchPage.html', context)

# ----------------handle Blog of Mine Page-------------------
def blog_ofMine(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    posts = Post.objects.filter(author= request.user)
    context = {'posts': posts,'current_user':current_user}
    return render(request, 'blog_ofMine.html', context)

# -----------------handle Profile Page-------------------
def Profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    DefaultProfile = get_object_or_404(UserProfile, id=user_id)
        
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=DefaultProfile)
        # save image and username to Comment
        # check form valid
        if form.is_valid():
            FormDB = form.save(commit=False)
            FormDB.id = user_id
            form.save()
            if DefaultProfile.image:
                Comment.objects.create(
                    user_id=current_user.id,
                    image=form.cleaned_data['image'],
                    username=current_user.username,
                )
                CommentChild.objects.create(
                    user_id=current_user.id,
                    image=form.cleaned_data['image'],

                    username=current_user.username,
                )
            messages.success(request, 'Lưu thông tin cá nhân thành công.')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=DefaultProfile)     

    context = { 'current_user': current_user, 'form': form, 'DefaultProfile': DefaultProfile}
    return render(request, 'Profile.html', context)
        

# -----------------handle Delete Post -------------------

def delete_post(request, post_id):
    if request.user.is_authenticated == False:
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Xóa bài post nếu yêu cầu là POST
        post.delete()
        return redirect('home')
# -----------------handle Update Post ------------------
        
def updatePost(request, post_id):
    if request.user.is_authenticated == False:
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    current_user = request.user if request.user.is_authenticated else None
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of the view for your home page
    else:
        form = PostForm(instance=post, initial={'image': post.image})
    # check current ủe is exit
    
    context = {'form': form,'current_user':current_user}
    return render(request, 'update.html', context)

def Category_page(request,category):
    current_user = request.user if request.user.is_authenticated else None
    category_item = Post.objects.filter(topic=category)
    category_topics = Post.objects.filter(topic=category).first()
    
    context ={'current_user': current_user,
              
              'category': category_item,'category_topics': category_topics,}
    return render(request, 'Categories.html', context)
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
    context = {'form': form,'current_user':current_user}
    return render(request, 'AddPost.html', context)
def AddPost_Citation(request,post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    current_user = request.user if request.user.is_authenticated else None
    url = 'http://127.0.0.1:8000/topic/'

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Tạo một instance của bài viết nhưng chưa lưu vào database
            post.author = request.user  # Gán tác giả là username của người dùng hiện tại
             # Lưu bài viết vào databas
            post.citation_url = url+str(post_id)+'/'
            post.save()
            return redirect('home')  # Chuyển hướng về trang chủ sau khi lưu bài viết thành công
    else:
        form = PostForm(initial={'citation_url': url+str(post_id)+'/'})
    context = {'form': form,'current_user':current_user}
    return render(request, 'citation.html', context)

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
                current_user = request.user if request.user.is_authenticated else None
                # Check if the user has a profile
                if not UserProfile.objects.filter(id=current_user.id).exists():
                    # Create a new profile for the user
                    UserProfile.objects.create(id = current_user.id)
                    
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
        
    context = {'form': form}
    return render(request, 'login.html', context)
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
    context = {'form': form}
    return render(request, 'register.html', context)
# logout
def user_logout(request):
    logout(request)
    return redirect('home')
# topic

def handle_like (request,user_id,post_id ):
    CMT = Comment.objects.get(id = user_id)
    if 'Like' in request.POST:
        CMT.like +=1
        redirect('topic', post_id)  
    elif "Dislike" in request.POST:
        CMT.like += 1
    
    CMT.save()
    return redirect('topic', post_id)
        

def handleLike_child (request, user_id,post_id):
    CMTChild = CommentChild.objects.get(user_id = user_id)
    if 'Like' in request.POST:
        CMTChild.like +=1
        return redirect('topic', post_id)
    elif "Dislike" in request.POST:
        CMTChild.like += 1
    CMTChild.save()    
    return redirect('topic', post_id)
        
def Topic(request,post_id):
    current_user = request.user if request.user.is_authenticated else None
    post = Post.objects.get(id=post_id)
    Post_Comment =Comment.objects.filter(topic_id=post_id) 
    comment_temp = CommentForm()
    #child
    Post_CommentChild =CommentChild.objects.filter(topic_id=post_id)
    commentChild_temp = CommentChildForm()
    Profiles = UserProfile.objects.all()
    
    relate_to = Post.objects.filter(topic=post.topic)
    context = {'post': post,'relate_to': relate_to,
               'current_user':current_user, 
               'Post_CommentChild': Post_CommentChild, 
                'comment_temp':comment_temp,
                'Post_Comments':Post_Comment,
                'commentChild_temp':commentChild_temp,
                
                'Profiles':Profiles
            }
    return render(request, 'topic.html', 
    context)
# Comment 
def Handle_Comment(request, post_id):
    current_user = request.user if request.user.is_authenticated else None
    if not request.user.is_authenticated:
        return redirect('login')
   
    # Lấy bài viết theo id  
    LengthCMTChild = len(Comment.objects.filter(topic_id=post_id))
    profile = get_object_or_404(UserProfile,id=current_user.id)
    if request.method == 'POST':
        comment_temp = CommentForm(request.POST)
        if comment_temp.is_valid():
            comment_DB = comment_temp.save(commit=False)
            comment_DB.topic_id = post_id
            comment_DB.user_id = current_user.id
            comment_DB.Commentid = LengthCMTChild
            comment_DB.comment_content = comment_temp.cleaned_data['comment_content']
            comment_DB.author = current_user
            
            if profile.image:
                comment_DB.image = profile.image
                comment_DB.username = profile.defaultName
            vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
            comment_DB.created_at = timezone.now().astimezone(vietnam_timezone)
            comment_DB.save()
            return redirect('topic', post_id)
            
            
    else:
        return redirect('topic', post_id)
    
    
 # -------------------handle Comment child---------------------
 
def Handle_CommentChild(request, post_id,comment_id):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    profile = get_object_or_404(UserProfile, id = current_user.id)
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
            CommentChild_DB.user_id = current_user.id
            CommentChild_DB.tag = ''
            CommentChild_DB.comment_content = comment_template.cleaned_data['comment_content']
            CommentChild_DB.author = current_user
            CommentChild_DB.commentChild_id = comment_id
            
            if profile.image:
                CommentChild_DB.image = profile.image
                CommentChild_DB.username = profile.defaultName
            CommentChild_DB.responder = responder
            CommentChild_DB.created_at  = timezone.now()
            if comment_id != current_user.id:
                Notification.objects.create(
                username = profile.defaultName,
                user_id = comment_id,
                message=str(comment_template.cleaned_data['comment_content']), 
                created_at=timezone.now(),
                image=profile.image,
                to='topic/%s/' % post_id  
                )
            CommentChild_DB.save()  
    return redirect('topic', post_id) 


 # -------------------handle Comment tag---------------------

def Handle_CommentTag(request, post_id,comment_id,user_id,comment_tag):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user if request.user.is_authenticated else None
    # CMT = CommentChild.objects.get()
    
    # Lấy bài viết theo id  
    
    profile = get_object_or_404(UserProfile, id = current_user.id)
    comment = Comment.objects.get(id = comment_id)
    comment.reply_count +=1
    comment.save(update_fields=['reply_count'])
    if request.method == 'POST':
        responder = request.POST.get('comment_author')
        comment_template = CommentChildForm(request.POST)
        if comment_template.is_valid():
            CommentChild_DB = comment_template.save(commit=False)
            CommentChild_DB.topic_id = post_id
            CommentChild_DB.user_id = current_user.id
            # Check to set user tag 
            if current_user.id == user_id:
                CommentChild_DB.tag = ''
            else:
                CommentChild_DB.tag = comment_tag
            CommentChild_DB.comment_content = comment_template.cleaned_data['comment_content']
            CommentChild_DB.author = current_user
            # handle Like
            
            if profile.image:
                CommentChild_DB.image = profile.image
                CommentChild_DB.username = profile.defaultName
            CommentChild_DB.commentChild_id = comment_id
            CommentChild_DB.responder = responder
            CommentChild_DB.created_at  = timezone.now()
            if user_id != current_user.id:
                Notification.objects.create(
                    username = profile.defaultName,
                    user_id = user_id,
                    message=str(comment_template.cleaned_data['comment_content']),
                    created_at=timezone.now(),
                    image=profile.image,
                    to='topic/%s/' % post_id  
                )
            CommentChild_DB.save()  
    return redirect('topic', post_id)
    

       
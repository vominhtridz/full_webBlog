from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# --------------------  BANNER HOME PAGE IMAGE -------------------   

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    
# --------------------  USER PROFILE -------------------  

    
        
class Notification(models.Model):
    username = models.CharField(default='user', max_length=100)
    user_id = models.IntegerField(default=1)
    message = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(default=timezone.now)
    to = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='profiles/images',default='/static/images/user-icon.png')
    

class UserProfile(models.Model):
    choices_gender= (
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Khác','Khác')
    )
    choices_day = [(i, i) for i in range(1, 32)]  # Days from 1 to 31
    choices_month = [(i, i) for i in range(1, 13)]  # Months from 1 to 12
    day = models.IntegerField( choices= choices_day,default=1)
    month = models.IntegerField( choices= choices_month,default=1)
    year = models.IntegerField(default=2010)
    address = models.CharField(max_length=200, blank=True, null=True,default='')
    phone_number = models.CharField(blank=True,max_length=11, null=True,default= '')
    defaultName = models.CharField(blank=True,max_length=30,default= 'User')
    image = models.ImageField(upload_to='profiles/images',default='/static/images/user-icon.png')
    email = models.EmailField(blank= True, default='example@gmail.com')
    gender = models.CharField(default='Nam', choices=choices_gender,max_length=20)
    def __str__(self):
        return self.defaultName
    


# ---------------------COMMENT FATER -------------------   
class Comment(models.Model):
    user_id = models.IntegerField(default= 1)
    Commentid = models.IntegerField(default=1)
    topic_id = models.IntegerField(default=1)
    comment_content = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)
    reply_count = models.IntegerField(default= 0,blank= True)
    like = models.IntegerField(default = 0)
    username= models.CharField(default= 'user',blank=True,max_length=50)
    image = models.ImageField(upload_to='comment/images',default='static/images/user-icon.png')

# --------------------  COMMENT CHILD -------------------   

class CommentChild(models.Model):
    tag = models.CharField(max_length=150,blank= True)
    user_id = models.IntegerField(default= 1)
    username= models.CharField(default= 'user',blank=True,max_length=50)
    image = models.ImageField(upload_to='comment/images',default='static/images/user-icon.png')
    topic_id = models.IntegerField(default=1)
    commentChild_id = models.IntegerField(default=1)
    responder = models.CharField(max_length=150)
    comment_content = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default = 0)
    
    
# -------------------------------------  POST  ---------------------------------   

class Post(models.Model):
    TOPIC_CHOICES = (
    ('du lịch', 'Du lịch'),
    ('thức ăn', 'Thức ăn'),
    ('công việc', 'Công việc'),
    ('giải trí', 'Giải trí'),
    )
    # lấy ra người dùng id đã đăng nhập hiện tại
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    citation_url = models.CharField(max_length=200, null=True,default= '')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Thêm trường image
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES, default='du_lịch')
    author = models.ForeignKey(User,on_delete= models.CASCADE,default='user')

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User


# --------------------  BANNER HOME PAGE IMAGE -------------------   

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    
# --------------------  USER PROFILE -------------------   
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
    year = models.IntegerField(default=2024)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(blank=True,max_length=11, null=True)
    defaultName = models.CharField(blank=True,max_length=30)
    image = models.ImageField(upload_to='profiles/images')
    email = models.EmailField(blank= True, default='example@gmail.com')
    gender = models.CharField(default='Nam', choices=choices_gender,max_length=20)
    def __str__(self):
        return self.defaultName
    


# ---------------------COMMENT FATER -------------------   
class Comment(models.Model):
    father = models.BooleanField(default= True)
    Commentid = models.IntegerField(default=1)
    topic_id = models.IntegerField()
    author = models.ForeignKey(User,default='',on_delete= models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_count = models.IntegerField(default= 0,blank= True)
    like = models.IntegerField(default = 0)
    

# --------------------  COMMENT CHILD -------------------   

class CommentChild(models.Model):
    tag = models.CharField(max_length=150,blank= True)
    topic_id = models.IntegerField()
    commentChild_id = models.IntegerField(default=1)
    responder = models.CharField(max_length=150)
    author = models.ForeignKey(User,default='',on_delete= models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
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
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Thêm trường image
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES, default='du_lịch')
    author = models.ForeignKey(User,default='',on_delete= models.CASCADE)

    def __str__(self):
        return self.title
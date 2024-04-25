from django.db import models

# Create your models here.
# cấu hình hình ảnh banner trang home
class Image(models.Model):
    image = models.ImageField(upload_to='images')

from django.db import models
# cấu hình bài blog
class Post(models.Model):
    TOPIC_CHOICES = (
    ('du lịch', 'Du lịch'),
    ('thức ăn', 'Thức ăn'),
    ('công việc', 'Công việc'),
    ('giải trí', 'Giải trí'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()  # Thêm trường date
    icon = models.CharField(max_length=100)  # Thêm trường icon
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Thêm trường image
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES, default='du_lịch')

    def __str__(self):
        return self.title
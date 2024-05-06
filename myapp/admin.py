from typing import Any
from django.contrib import admin
from myapp.models import Image
from myapp.models import Post
from myapp.models import Comment
from myapp.models import CommentChild
from myapp.models import UserProfile
# Register your models here.
admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentChild)
admin.site.register(UserProfile)
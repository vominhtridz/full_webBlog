from django.contrib import admin
from myapp.models import Image
from myapp.models import Post

# Register your models here.

admin.site.register(Image)
admin.site.register(Post)
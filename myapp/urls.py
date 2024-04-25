from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.Category_page, name='Category_page'),
    path('topic/<int:post_id>/', views.Topic, name='topic'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
     path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('update/<int:post_id>/', views.updatePost, name='update_post'),
    path('addpost/', views.AddPost, name='addpost'),
    path('logout/', views.user_logout, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
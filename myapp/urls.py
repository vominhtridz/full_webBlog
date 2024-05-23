from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.Category_page, name='Category_page'),
    path('blog/mine/', views.blog_ofMine, name='Category_page'),
    path('topic/<int:post_id>/', views.Topic, name='topic'),
    path('comment/<int:post_id>/', views.Handle_Comment, name='comment'),
    path('comment_child/<int:post_id>/<int:comment_id>/', views.Handle_CommentChild, name='comment_child'),
    path('like/<int:post_id>/<int:comment_id>/', views.handleLike, name='like'),
    path('like_child/<int:post_id>/<int:commentChild_id>/', views.handleLikeChild, name='like_child'),
    path('comment_tag/<int:post_id>/<int:comment_id>/<int:user_id>/<str:comment_tag>/', views.Handle_CommentTag, name='comment_tag'),
    path('login/', views.login, name='login'),
    path('user/profile/<int:user_id>/', views.Profile, name='Profile'),
    path('search/<str:search_value>/', views.SearchPage, name='SearchPage'),
    path('register/', views.register, name='register'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('update/<int:post_id>/', views.updatePost, name='update_post'),
    path('addpost/', views.AddPost, name='addpost'),
    path('addpost/<int:post_id>/', views.AddPost_Citation, name='addpost'),
    path('logout/', views.user_logout, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
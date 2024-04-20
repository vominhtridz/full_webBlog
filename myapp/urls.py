from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('nike/', views.nike, name='nike'),
    path('adidas/', views.Adidas, name='Adidas'),
    path('puma/', views.Puma, name='Puma'),
    path('asics/', views.Asics, name='Asics'),
    path('pelock/', views.Pelock, name='Pelock'),
    path('product/', views.InforProduct, name='inforProduct'),
    path('cart/', views.Cart, name='cart'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('payment/', views.payment, name='payment'),
    path('logout/', views.user_logout, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from myapp.models import Notification
from myapp.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from myapp.models import Post
from django.utils import timezone





def ProfileContext(request):
    current_user = request.user if request.user.is_authenticated else None
    profile = None
    if current_user:
        try:
            profile = UserProfile.objects.get(id=current_user.id)     
        except ObjectDoesNotExist:
            profile = None             
    else:
        profile= None   
        
    return {'profile': profile}
    
def NotificationContext(request):
    current_time = timezone.now()
    current_user = request.user if request.user.is_authenticated else None
    user_notifications = None 
    time_calculated = '6 tiếng trước'
    
    if current_user:
        try:
            user_notifications = Notification.objects.filter(user_id=current_user.id)
        except ObjectDoesNotExist:
            user_notifications = None 
    else:
        user_notifications = None
    
    # Iterate over notifications to calculate time differences, assuming you have a timestamp field named 'created_at'
    
    # Print user_notifications for debugging purposes
    
    return {'Notification': user_notifications}
def PostContext(request):
    posts = Post.objects.all()
    return {'posts': posts}



from django.urls import path
from user.views import register_user, login_user, confirm_user

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('confirm/', confirm_user, name='confirm_user'),
]
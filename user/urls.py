


from django.urls import path
from user.views import authenticate_api_view, registration_api_view

urlpatterns = [
    path('registration/', registration_api_view, name='registration-api-view'),
    path('authentication/', authenticate_api_view, name= 'authentication-api-view'),
]
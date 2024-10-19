from django.urls import path
from .views import signup, login, test_token

urlpatterns = [
    #path('users/', get_users, name='get_users'),
    path('users/signup/', signup, name='signup'),
    path('users/login/', login, name='login'),
    path('users/test_token/', test_token, name='test_token')
]
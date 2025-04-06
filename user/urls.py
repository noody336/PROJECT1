from django.urls import path
from .views import *

urlpatterns = [
    path('reg-form/', registration, name = 'registr'),
    path('login-form/', user_login, name = 'login'),
    path('logout', user_logout, name = 'logout'),
]
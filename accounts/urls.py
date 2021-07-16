
# from django.contrib.auth.models import User
from knox import views as knox_views
from accounts.views import RegisterAPI, LoginAPI, UserAPI
from django.urls import path

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login'),
    path('register', RegisterAPI.as_view(), name='register'),
    path('user', UserAPI.as_view(), name='user'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

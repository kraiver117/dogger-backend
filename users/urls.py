# Django 
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route='users',
        view=views.userProfiles_list,
        name='users'
    ),
    path(
        route='users/<int:pk>',
        view=views.user_detail,
        name='users'
    )
]
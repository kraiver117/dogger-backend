# Django 
from django.urls import path

# Views
from walkers import views

urlpatterns = [
    path(
        route='walkers',
        view=views.GET_POST_USER,
        name='walkers'
    ),
    path(
        route='walkers/<int:pk>',
        view=views.GET_PUT_DELETE_USER,
        name='walkers'
    )
]
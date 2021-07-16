from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('walks', views.GET_POST_WALK, name='walks'),
    path('walks/<int:pk>', views.GET_PUT_DELETE_WALK, name='walks'),
    path('walks/walker/<int:pk_walker>', views.GET_WALKS_BY_WALKER, name='walks'),
]

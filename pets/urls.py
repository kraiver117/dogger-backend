from django.urls import path
from . import views

urlpatterns = [
    path('pets', views.getPost_pet, name='pets'),
    path('pets/<int:pk>', views.deletePostGet_pet, name='pets'),
    path('pets/owner/<int:pk_user>', views.get_pets_by_owner, name='pets'),

]

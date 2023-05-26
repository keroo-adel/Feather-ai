from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/create/', views.UserCreateAPIView.as_view(), name='create_user'),

]
from products.views import user
from django.urls import path

path('users/', user.UserList.as_view()),
path('users/<int:pk>/', user.UserDetail.as_view()),

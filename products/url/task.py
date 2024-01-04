from django.urls import path, include
from products.views import task, user
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', task.TaskList.as_view()),
    path('tasks/<int:pk>/', task.TaskDetail.as_view()),
    path('users/', user.UserList.as_view()),
    path('users/<int:pk>/', user.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

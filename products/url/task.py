from django.urls import path
from products.views import task
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', task.TaskList.as_view()),
    path('tasks/<int:pk>/', task.TaskDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from products.views import task
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', task.task_list),
    path('tasks/<int:pk>/', task.task_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
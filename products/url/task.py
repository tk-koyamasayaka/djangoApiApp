from django.urls import path
from products.views import task

urlpatterns = [
    path('tasks/', task.task_list),
    path('tasks/<int:pk>/', task.task_detail)
]
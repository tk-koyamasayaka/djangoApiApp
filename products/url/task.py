from django.urls import path
from products.views.task import TaskList

urlpatterns = [
    path('tasks/', TaskList.as_view())
]
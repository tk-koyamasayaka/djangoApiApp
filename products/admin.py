from django.contrib import admin
from products.models.tasks import Task

# Register your models here.
admin.site.register(Task)

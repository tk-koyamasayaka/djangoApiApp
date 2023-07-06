from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(verbose_name='内容',blank=True,null=True,max_length=500)
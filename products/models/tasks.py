from django.db import models


class Task(models.Model):
    content = models.TextField(verbose_name="内容", blank=False, null=False, max_length=500)
    due_date = models.DateTimeField(verbose_name="期限日", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # TODO: abstract classで定義する
    update_at = models.DateTimeField(auto_now_add=True)  # TODO: abstract classで定義する

    def __str__(self):
        return self.content

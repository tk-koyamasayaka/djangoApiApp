from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Task(models.Model):
    content = models.TextField(verbose_name="内容", blank=False, null=False, max_length=500)
    due_date = models.DateTimeField(verbose_name="期限日", null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    highlighted = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.highlighted = 'パワー'
        super().save(*args, **kwargs)

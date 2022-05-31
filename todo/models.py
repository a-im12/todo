from django.db import models

from acounts.models import CustomUser

class TodoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザ',
        on_delete=models.CASCADE
    )
    
    todo = models.TextField(
        verbose_name='ToDo',
    )
    
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.todo

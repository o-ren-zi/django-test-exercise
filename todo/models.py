from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')  # タスクとの関連
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]  # 最初の20文字だけ表示


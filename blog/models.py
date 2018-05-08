from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # 글쓴이
    auther = models.ForeignKey('auth.user')
    # 글제목
    title = models.CharField(max_length=100)
    # 내용
    content = models.TextField()
    # 등록일
    create_at = models.DateTimeField(default=timezone.now)
    # 수정일
    update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.create_at = timezone.now()
        self.save()




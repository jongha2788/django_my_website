from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# user 라는 객체 이미 제공됨
 # 사용자 james 가 삭제 되었을 때 글 쓴 거 삭제 해줌

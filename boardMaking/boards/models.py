from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    userName = models.CharField(max_length=8)
    create_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)


# 우리가 어떤 게시글이라는 DB가 생성 되었을때
# 게시글들 중에 유일함을 나타내는 것은 id == pk  ㅇㅋ?
# Board의 자식인 Comment랑 Board랑 이어주는것은 ForeignKe로
# Board의 id 값으로 이어주게 됨

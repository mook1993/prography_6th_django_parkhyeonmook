from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=30) # 제목
    description = models.CharField(max_length=500) # 내용
    created_at = models.DateTimeField(null=False)



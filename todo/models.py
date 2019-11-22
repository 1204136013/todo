from django.db import models


# Create your models here.
class Todo(models.Model):
    # 会隐式创建 id
    title = models.CharField(max_length=100)
    completed = models.BooleanField(null=False, default=False)

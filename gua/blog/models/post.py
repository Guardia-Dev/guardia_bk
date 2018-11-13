from django.db import models

from .tag import Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField("文章标题", max_length=128, null=False, blank=False, unique=True)
    author = models.CharField("作者", max_length=128)
    body = models.TextField("内容")

    tag = models.ManyToManyField("所属标签", Tag)


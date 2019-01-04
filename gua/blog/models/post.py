from django.db import models

from blog.models.tag import Tag
from blog.models.category import Category


# Create your models here.
class Post(models.Model):
    title = models.CharField("文章标题", max_length=128, null=False, blank=False, unique=True)
    author = models.CharField("作者", max_length=128)
    body = models.TextField("内容")

    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("上次修改时间", auto_now=True)

    tag = models.ManyToManyField(Tag, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        s = "{title} - {author}, {date}"
        return s.format(title=self.title, author=self.author, date=str(self.created_at))

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = verbose_name

        unique_together = (
            ('title', 'author'),
        )

        index_together = [
            ['title'],
        ]

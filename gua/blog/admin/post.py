from django.contrib import admin

from blog.models import Post
from blog.admin.tag import TagInline


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'body',
        'category',
    ]

    inlines = [
        TagInline,
    ]

    exclude = (
        'tag',
    )

    list_filter = []

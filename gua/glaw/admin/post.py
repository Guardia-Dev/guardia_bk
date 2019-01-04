from django.contrib import admin

from ..models import post


@admin.register(post.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'body',
        'category',
    ]

    list_filter = [
    ]

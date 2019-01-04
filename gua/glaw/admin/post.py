from django.contrib import admin

from ..models import post


class TagInline(admin.TabularInline):
    model = post.Post.tag.through
    extra = 1


@admin.register(post.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'origin_title',
        'author',
        'body',
    ]

    inlines = [
        TagInline,
    ]

    list_filter = [
    ]

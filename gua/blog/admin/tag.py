from django.contrib import admin

from blog.models import Tag
from blog.models import Post


class TagInline(admin.TabularInline):
    model = Post.tag.through
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]

    list_display = [
        'name',
        'color',
    ]

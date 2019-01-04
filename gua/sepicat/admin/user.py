from django.contrib import admin

from ..models import user


@admin.register(user.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'login',
        'nickname',
    ]

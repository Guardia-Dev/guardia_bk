# Generated by Django 2.1.4 on 2019-01-07 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glaw', '0004_post_published_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='origin_url',
            new_name='html_url',
        ),
    ]
# Generated by Django 2.1.4 on 2019-01-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glaw', '0002_auto_20190104_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '成员', 'verbose_name_plural': '成员'},
        ),
        migrations.AddField(
            model_name='post',
            name='github_url',
            field=models.URLField(blank=True, max_length=128, null=True, verbose_name='GitHub 链接'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Twitter'),
        ),
    ]

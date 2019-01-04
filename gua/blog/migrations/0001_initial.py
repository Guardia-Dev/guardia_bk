# Generated by Django 2.1.3 on 2018-11-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='文章标题')),
                ('author', models.CharField(max_length=128, verbose_name='作者')),
                ('body', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
            ],
            options={
                'verbose_name': '博文',
                'verbose_name_plural': '博文',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='标签名')),
                ('color', models.IntegerField(verbose_name='标签颜色')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'author')},
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together={('title',)},
        ),
    ]
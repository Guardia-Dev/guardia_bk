# Generated by Django 2.1.4 on 2019-01-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glaw', '0003_auto_20190105_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now=True, verbose_name='译文发布时间'),
        ),
    ]

from django.db import models

class User(models.Model):
    login = models.CharField("用户 login", max_length=128, null=False, blank=False, unique=True)
    nickname = models.CharField("昵称", max_length=128, null=False, blank=False)

    def __str__(self):
        s = "{login} ({nickname})"
        return s.format(login=self.login, nickname=self.nickname)

    

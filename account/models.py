import hashlib
from pyexpat import model

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    openid = models.CharField(
        verbose_name=_('微信OpenID'), help_text=_('微信OpenID'), max_length=100, unique=True, null=True, blank=True)
    avatar_url = models.URLField(
        verbose_name=_('头像'), help_text=_('头像'), null=True, blank=True)
    nick_name = models.CharField(
        verbose_name=_('昵称'), help_text=_('昵称'), max_length=100, null=True, blank=True, unique=True)
    gender = models.SmallIntegerField(
        verbose_name=_('性别'), help_text=_('性别'), choices=((1, '男'), (2, '女'), (0, '未知')), null=True, blank=True)
    desc = models.TextField(verbose_name=_('描述'), help_text=_('描述'), max_length=2000, null=True, blank=True)
    can_use = models.BooleanField(verbose_name=_('是否可用'), default=False)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def create_username_password(self):
        if not self.username and not self.password and self.openid:
            key = settings.SECRET_KEY
            self.username = hashlib.pbkdf2_hmac(
                "sha256", getattr(self, 'openid').encode(encoding='utf-8'), key.encode(encoding='utf-8'), 10).hex()
            self.password = hashlib.pbkdf2_hmac(
                "sha256", self.username.encode(), getattr(self, 'openid').encode(encoding='utf-8'), 10).hex()

    def save(self, *args, **kwargs):
        self.create_username_password()
        super().save(*args, **kwargs)

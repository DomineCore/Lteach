from statistics import mode
from tabnanny import verbose
from django.db import models

from account.models import User

class Guardian(models.Model):
    name = models.CharField(verbose_name="监护人姓名",max_length=10)
    phone = models.CharField(verbose_name="监护人手机号", max_length=11)
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)

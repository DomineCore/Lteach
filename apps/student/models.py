from django.db import models

from apps.guardian.models import Guardian
from common.constants import GENDER

class Student(models.Model):
    name = models.CharField(verbose_name="学生姓名", max_length=10)
    gender = models.CharField(choices=GENDER, verbose_name="性别", max_length=1)
    guardian = models.ForeignKey(Guardian, verbose_name="监护人", null=True, on_delete=models.SET_NULL)
    birth = models.DateField(verbose_name="出生日期")
    address = models.CharField(verbose_name="家庭住址", max_length=255)
    
    class Meta:
        unique_together = ("guardian", "name")

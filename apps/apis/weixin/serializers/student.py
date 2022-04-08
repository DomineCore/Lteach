from rest_framework import serializers

from apps.student.models import Student
from apps.apis.weixin.serializers.guardian import GuardianSerializer
from common.constants import GENDER

class StudentRegisterSerializer(serializers.Serializer):
    name = serializers.CharField(help_text="学生姓名")
    guardian_name = serializers.CharField(help_text="监护人姓名")
    gender = serializers.ChoiceField(GENDER, help_text="性别")
    birth = serializers.DateField(help_text="学生出生日期")
    address = serializers.CharField(help_text="家庭住址")
    phone = serializers.CharField(help_text="监护人手机号")

class StudentSerializer(serializers.ModelSerializer):
    guardian = GuardianSerializer()
    class Meta:
        model = Student
        fields = "__all__"
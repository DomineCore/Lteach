from rest_framework import serializers

from common.weixin.helpers import get_openid
from account.models import User

class WxLoginSerializer(serializers.Serializer):
    code = serializers.CharField()

    def save(self):
        # getopenid
        openid = get_openid(self.validated_data["code"])
        # 校验用户是否存在
        user = User.objects.filter(openid=openid).first()
        if not user:
            # 创建用户
            user = User(openid=openid)
            user.save()
        return user
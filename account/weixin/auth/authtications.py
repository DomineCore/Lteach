from tkinter.messagebox import NO
from rest_framework.authentication import BaseAuthentication

from account.models import User

class WeixinAuthentication(BaseAuthentication):
    def authenticate(self, request):
        openid = request.headers.get("openid")
        if not openid:
            return None
        try:
            user = User.objects.get(openid=openid)
        except User.DoesNotExist:
            return None
        return (user, None)
    def authenticate_header(self, request):
        return "401 认证失败"
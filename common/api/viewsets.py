from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import permissions

from common.api.mixins import LoginExemptMixin,ApiMixin
from account.weixin.auth.authtications import WeixinAuthentication

class LoginExemptViewSet(GenericViewSet,LoginExemptMixin,ApiMixin):
    """
    免登陆的viewset
    """
    pass

class BcloudViewSet(ModelViewSet,ApiMixin):
    """
    需要登录的viewset
    """
    pass

class WeixinMixin(ApiMixin):
    authentication_classes = [WeixinAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class WxGenericViewSet(GenericViewSet, WeixinMixin):
    pass

class WeixinModelViewSet(ModelViewSet, WeixinMixin):
    pass
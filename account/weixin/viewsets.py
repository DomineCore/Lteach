from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from common.api.mixins import ApiMixin

from account.weixin.serializer import WxLoginSerializer

class WxLogin(GenericViewSet, ApiMixin):
    serializer_class = WxLoginSerializer
    permission_classes = ()
    authentication_classes = ()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"openid":user.openid},status=status.HTTP_201_CREATED)
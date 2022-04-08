from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.apis.weixin.viewsets.student import WxStudentViewSet

api_v1= DefaultRouter()
weixin_api_v1 = DefaultRouter()

# api_v1.register()

weixin_api_v1.register("student", WxStudentViewSet)

url_custom = [
    url(r'^api/v1/', include(api_v1.urls)),
    url(r'^weixin/v1/', include(weixin_api_v1.urls))
]
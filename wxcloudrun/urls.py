"""wxcloudrun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from account.views import LoginView
from account.weixin.viewsets import WxLogin
from apps.test import test_view
from apps.urls import url_custom


urlpatterns = [
    # 登录相关
    url(r'^login/', LoginView.as_view()),
    url(r'^weixin/login/', WxLogin.as_view({"post":"create"})),
    url(r'^test/', test_view)
] + url_custom

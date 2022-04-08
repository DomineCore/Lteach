import requests
import logging

from django.conf import settings

logger = logging.getLogger("log")


def get_openid(code):
    try:
        resp = requests.get(
            url=settings.WX_AUTH_URL,
            params={
                "appid":settings.WX_APPID,
                "secret":settings.WX_APP_SECRET,
                "grant_type":settings.WX_AUTH_GRANT_TYPE,
                "js_code":code
            }
        ).json()
        openid = resp["openid"]
        return openid
    except Exception as e:
        logger.exception("获取openid发生异常:"+str(e))
        raise Exception
        
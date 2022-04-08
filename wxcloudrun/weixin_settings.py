import os
# 小程序
WX_APPID = os.getenv("WX_APPID")
WX_APP_SECRET = os.getenv("WX_APP_SECRET")
WX_AUTH_GRANT_TYPE = os.getenv("WX_AUTH_GRANT_TYPE","authorization_code")
WX_AUTH_URL = os.getenv("WX_AUTH_URL", "https://api.weixin.qq.com/sns/jscode2session")
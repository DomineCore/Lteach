def login_exempt(view_func):
    """
    FBV登录豁免
    """
    def wrap(*args, **kwargs):
        view_func.authentication_classes = []
        view_func.permission_classes = []
        return view_func(*args, **kwargs)
    return wrap


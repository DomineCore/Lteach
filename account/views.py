from datetime import datetime
from django.conf import settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            expiration = (datetime.utcnow() +
                            api_settings.JWT_EXPIRATION_DELTA)
            response.set_cookie(settings.JWT_AUTH_COOKIE,
                                token,
                                expires=expiration)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

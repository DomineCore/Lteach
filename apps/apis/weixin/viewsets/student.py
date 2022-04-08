from configparser import DuplicateOptionError
import logging

from django.db.transaction import atomic
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail

from common.api.viewsets import WxGenericViewSet
from common import err_code
from apps.student.models import Student
from apps.guardian.models import Guardian
from apps.apis.weixin.serializers.student import (
    StudentRegisterSerializer,
    StudentSerializer
)

logger = logging.getLogger("log")

class WxStudentViewSet(WxGenericViewSet, mixins.CreateModelMixin):
    queryset = Student.objects.all()

    serializer_class = StudentRegisterSerializer

    def get_queryset(self):
        return Student.objects.filter(guardian__user=self.request.user)

    @action(["POST"], detail=False)
    def register(self, request, *args, **kwargs):
        # valid
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with atomic():
                # create guardian
                guardian_name = serializer.validated_data.pop("guardian_name")
                phone = serializer.validated_data.pop("phone")
                user = request.user
                guardian = Guardian.objects.create(name=guardian_name,phone=phone,user=user)
                # create student
                name = serializer.validated_data.pop("name")
                address = serializer.validated_data.pop("address")
                birth = serializer.validated_data.pop("birth")
                student = Student.objects.create(name=name,guardian=guardian,birth=birth,address=address)
                serializer_res = StudentSerializer(instance=student)
                return Response(data=serializer_res.data)
        except Exception as e:
            message = "注册学员失败"
            logger.exception(message,str(e))
            return Response({"detail": ErrorDetail(message, err_code.UNKNOWN_ERROR.code)}, exception=True)

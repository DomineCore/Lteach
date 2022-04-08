from rest_framework import serializers

from apps.guardian.models import Guardian

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        exclude = ["user"]
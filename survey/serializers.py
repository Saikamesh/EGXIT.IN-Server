from rest_framework import serializers
from .models import MainReasons, WorkExperienceMetrics, AdditionalResponse, User


class MainReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainReasons
        fields = "__all__"


class WorkExperienceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperienceMetrics
        fields = "__all__"


class AdditionalResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalResponse
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

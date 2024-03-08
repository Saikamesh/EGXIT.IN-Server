from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    MainReasonSerializer,
    WorkExperienceMetricsSerializer,
    AdditionalResponseSerializer,
)
from .models import MainReasons, WorkExperienceMetrics, AdditionalResponse


@api_view(["POST"])
def insert_main_reasons(request):
    serializer = MainReasonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def insert_work_experience_metrics(request):
    serializer = WorkExperienceMetricsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def insert_additional_response(request):
    serializer = AdditionalResponseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# @api_view(["DELETE"])
# def clear_all_data(request):
#     MainReasons.objects.all().delete()
#     WorkExperienceMetrics.objects.all().delete()
#     AdditionalResponse.objects.all().delete()
#     return Response("All data cleared", status=200)

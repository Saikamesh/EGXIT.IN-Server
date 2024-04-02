from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    MainReasonSerializer,
    WorkExperienceMetricsSerializer,
    AdditionalResponseSerializer,
    # UserSerializer,
)
from .models import MainReasons, WorkExperienceMetrics, AdditionalResponse, User
from django.db.models import Q
from collections import OrderedDict


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


@api_view(["GET"])
def get_top_influences(request):
    influences = MainReasons.objects.values_list("influence", flat=True)
    influences_list = [influence for sublist in influences for influence in sublist]
    influences_dict = {}
    for influence in influences_list:
        if influence in influences_dict:
            influences_dict[influence] += 1
        else:
            influences_dict[influence] = 1
    top_influences = sorted(influences_dict.items(), key=lambda x: x[1], reverse=True)
    return Response(top_influences, status=200)


# get the agreed & most agreed upon work experience metrics
@api_view(["GET"])
def get_workmetrics(request):
    work_metrics = WorkExperienceMetrics.objects.values()
    agreed_metrics = {}
    for metric in work_metrics:
        for key, value in metric.items():
            if key != "id":
                if key in agreed_metrics:
                    agreed_metrics[key] += value
                else:
                    agreed_metrics[key] = value

    # agreed_metrics = sorted(agreed_metrics.items(), key=lambda x: x[1], reverse=True)
    agreed_metrics = agreed_metrics.items()  # unsorted
    return Response(agreed_metrics, status=200)


@api_view(["GET"])
def get_metrics_count(request):
    work_metrics = WorkExperienceMetrics.objects.values()
    metrics_dict = OrderedDict()

    # Initialize all ratings to 0
    for key in work_metrics[0].keys():
        if key != "id":
            metrics_dict[key] = OrderedDict((str(i), 0) for i in range(1, 6))

    # Count the occurrences of each metric value
    for metric in work_metrics:
        for key, value in metric.items():
            if key != "id":
                metrics_dict[key][str(value)] = metrics_dict[key].get(str(value), 0) + 1

    return Response(metrics_dict, status=200)

# @api_view(["DELETE"])
# def clear_all_data(request):
#     MainReasons.objects.all().delete()
#     WorkExperienceMetrics.objects.all().delete()
#     AdditionalResponse.objects.all().delete()
#     return Response("All data cleared", status=200)


# @api_view(["POST"])
# def user_signup(request):
#     email = request.data.get("email")
#     password = request.data.get("password")

#     if not email or not password:
#         return Response({"Email and password are required"}, status=400)

#     try:
#         user = User.objects.get(Q(email=email) | Q(password=password))
#         return Response({"User already exists"}, status=400)
#     except User.DoesNotExist:
#         user = User.objects.create(email=email, password=password)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=201)


# @api_view(["POST"])
# def login(request):
#     pass
from django.urls import path
from survey import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mainreasons", views.insert_main_reasons, name="mainreasons"),
    path("workexperiencemetrics", views.insert_work_experience_metrics, name="workexperiencemetrics"),
    path("additionalresponse", views.insert_additional_response, name="additionalresponse"),
    ]

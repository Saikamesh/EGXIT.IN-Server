from django.urls import path
from survey import views

urlpatterns = [
    path("mainreasons", views.insert_main_reasons, name="mainreasons"),
    path("workexperiencemetrics", views.insert_work_experience_metrics, name="workexperiencemetrics"),
    path("additionalresponse", views.insert_additional_response, name="additionalresponse"),
    # path("clear", views.clear_all_data, name="clear")
    ]

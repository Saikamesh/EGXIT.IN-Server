from django.urls import path
from survey import views

urlpatterns = [
    # path("signup", views.user_signup, name="signup"),
    path("mainreasons", views.insert_main_reasons, name="mainreasons"),
    path("workexperiencemetrics", views.insert_work_experience_metrics, name="workexperiencemetrics"),
    path("additionalresponse", views.insert_additional_response, name="additionalresponse"),
    path("topinfluences", views.get_top_influences, name="topinfluences"),
    path("agreedworkmetrics", views.get_workmetrics, name="agreedworkmetrics"),
    path("metrics", views.get_metrics_count, name="metrics"),
    # path("clear", views.clear_all_data, name="clear")
    ]

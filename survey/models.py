from django.db import models
from django.core.validators import RegexValidator


class MainReasons(models.Model):
    position: str = models.CharField(max_length=30)
    influence: str = models.JSONField(default=list)
    additional_reflection: str = models.CharField(max_length=500, blank=True)


class WorkExperienceMetrics(models.Model):
    Support_Professional_Development: int = models.IntegerField()
    Career_Growth_Opportunities: int = models.IntegerField()
    Accomplishment_Recognition: int = models.IntegerField()
    Work_Life_Balance_Consideration: int = models.IntegerField()
    Collegial_Work_Environment: int = models.IntegerField()
    DEI_Commitment: int = models.IntegerField()
    College_Diversity: int = models.IntegerField()
    Department_Diversity: int = models.IntegerField()
    Mentoring_Opportunities: int = models.IntegerField()
    Social_Networking_Support: int = models.IntegerField()
    Contribution_Recognition: int = models.IntegerField()
    Experience_Valuation: int = models.IntegerField()
    Collaboration_Opportunities: int = models.IntegerField()
    Openness_to_New_Ideas: int = models.IntegerField()
    Integration_into_Community: int = models.IntegerField()
    Compensation: int = models.IntegerField()
    Health_Benefits: int = models.IntegerField()
    Other_College_Benefits: int = models.IntegerField()


class AdditionalResponse(models.Model):
    WorkExpDesc: str = models.CharField(max_length=500, blank=True)
    CollegeExpDesc: str = models.CharField(max_length=500, blank=True)
    InPersonInterview: str = models.CharField(max_length=3)
    FullName: str = models.CharField(max_length=50, blank=True)
    Email: str = models.EmailField(max_length=50, blank=True)
    Phone: str = models.CharField(
        max_length=10, blank=True, validators=[RegexValidator(r"^\d{10}$")]
    )


class User(models.Model):
    email: str = models.EmailField(max_length=50)
    password: str = models.CharField(max_length=50)

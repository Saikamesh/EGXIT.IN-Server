from django.contrib import admin
from .models import MainReasons, WorkExperienceMetrics, AdditionalResponse


class MainReasonsAdmin(admin.ModelAdmin):
    pass


class WorkExperienceMetricsAdmin(admin.ModelAdmin):
    pass


class AdditionalResponseAdmin(admin.ModelAdmin):
    pass


admin.site.register(MainReasons)
admin.site.register(WorkExperienceMetrics)
admin.site.register(AdditionalResponse)

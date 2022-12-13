import django_filters

from . models import *


class HealthFormFilter(django_filters.FilterSet):
    class Meta:
        model = HealthForm
        fields = ['traveled_within_last_two_weeks', 'experiencing_symptoms']

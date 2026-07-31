from  rest_framework import serializers
from job_vacancy.models import JobVacancy

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=JobVacancy
        field=' all '
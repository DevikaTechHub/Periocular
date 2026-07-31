from  rest_framework import serializers
from job_application.models import JobApplication

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=JobApplication
        field=' all '
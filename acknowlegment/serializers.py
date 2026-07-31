from  rest_framework import serializers
from acknowlegment.models import Acknowledgment

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=Acknowledgment
        field=' all '
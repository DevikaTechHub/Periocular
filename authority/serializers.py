from  rest_framework import serializers
from authority.models import Authority

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=Authority
        field=' all '
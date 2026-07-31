from  rest_framework import serializers
from cert_request.models import CertRequest

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=CertRequest
        field=' all '
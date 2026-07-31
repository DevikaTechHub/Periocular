from  rest_framework import serializers
from cert_details.models import CertDetails

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=CertDetails
        field=' all '
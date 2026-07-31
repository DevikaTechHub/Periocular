from  rest_framework import serializers
from user.models import User

class android_serializer(serializers.ModelSerializer):
    class meta:
        model=User
        field='__all__'
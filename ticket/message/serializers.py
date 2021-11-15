from rest_framework import serializers
from message.models import Credentials


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = '__all__'




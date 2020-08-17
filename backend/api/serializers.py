from rest_framework import serializers
from .models import secret


class secretSerializer(serializers.ModelSerializer):
    class Meta:
        model = secret
        fields = ('name', 'password', 'expired', 'created_at', 'uuid', 'access_code')

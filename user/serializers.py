from rest_framework import serializers
from .models import details

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= details
        fields='__all__'


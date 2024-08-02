from rest_framework import serializers
from .models import UniData

class UniDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniData
        fields = ['id', 'web_pages', 'country', 'state_province', 'domains', 'alpha_two_code', 'name']

from rest_framework import serializers
from .models import Lead


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'name', 'phone', 'source', 'message']

    def validate(self, data):
        if not data.get('phone'):
            raise serializers.ValidationError("Телефон или email обязателен.")
        return data

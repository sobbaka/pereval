from rest_framework import serializers
from app.models import PerevalAdded

class PerevalAddedSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalAdded
        fields = [
            'date_added',
            'raw_data',
            'images'
        ]
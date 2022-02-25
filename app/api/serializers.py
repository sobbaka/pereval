from rest_framework import serializers
from django.db import models
from app.models import PerevalAdded
from django.contrib.postgres.fields import ArrayField


class PerevalAddedSpecial(models.Model):
    id = models.TextField()
    beautyTitle = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField()
    user = models.TextField()
    coords = models.TextField()
    type = models.TextField()
    level = models.TextField()
    images = ArrayField(models.CharField(max_length=200), blank=True)


class PerevalAddedSpecialSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalAddedSpecial
        fields = [
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'user',
            'coords',
            'type',
            'level',
            'images'
        ]


class PerevalAddedSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalAdded
        fields = [
            'date_added',
            'raw_data',
            'images'
        ]
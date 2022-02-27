from rest_framework import serializers
from app.models import PerevalAdded
from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


from drf_yasg import openapi

class PerevalSchema(models.Model):
    raw_data = JSONField()


class RawDataField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "properties": {
                "id": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "beautyTitle": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "other_titles": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "connect": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "add_time": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "user":  openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                ),
                "coords": {
                    "type": openapi.TYPE_OBJECT,
                    "properties": {
                        "latitude": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "longitude": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "height": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                    }
                },
                "type": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "level": {
                    "type": openapi.TYPE_OBJECT,
                    "properties": {
                        "winter": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "summer": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "autumn": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "spring": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                    }
                },
                "images": {
                    "type": openapi.TYPE_ARRAY,
                    "items": {
                        "type": openapi.TYPE_OBJECT,
                        "properties": {
                            "url": openapi.Schema(
                                type=openapi.TYPE_STRING,
                            ),
                            "title": openapi.Schema(
                                type=openapi.TYPE_STRING,
                            ),
                        }
                    }
                }
            },
            "required": ["subject", "body"],
         }

class PerevalSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalSchema
        fields = "__all__"

    raw_data = RawDataField()


class PerevalAddedSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalAdded
        fields = [
            'date_added',
            'raw_data',
            'images'
        ]
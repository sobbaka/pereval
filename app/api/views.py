from jsonschema.validators import Draft7Validator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
from datetime import datetime

from app.models import PerevalImages, PerevalAdded
from app.api.serializers import PerevalAddedSerializer, PerevalSchemaSerializer, PerevalAddedSpecialSerializer
from app.schema import schema

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(methods=['post',], request_body=PerevalSchemaSerializer)
@api_view(['POST', ])
def api_recieve_data(request):

    if request.method == 'POST':

        valid = Draft7Validator(schema).is_valid(request.data)

        if not valid:
            errors_lst = [error.message for error in Draft7Validator(schema).iter_errors(request.data)]
            errors = {'validation_errors': errors_lst}
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_added_str = request.data.pop("add_time")
            date_added = datetime.strptime(date_added_str, '%Y-%m-%d %H:%M:%S')

        except Exception:
            data = {"add_time": "datetime is invalid. Valid example 2021-09-22 13:18:13"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        images = request.data.pop("images")

        pereval_added_images = {}
        for image in images:
            image_obj = PerevalImages.objects.create(date_added=date_added, img=image["url"])

            if image["title"] in pereval_added_images.keys():
                pereval_added_images[image["title"]].append(image_obj.id)
            else:
                pereval_added_images[image["title"]] = [image_obj.id, ]

        images = json.dumps(pereval_added_images,
                            sort_keys=False,
                            indent=4,
                            ensure_ascii=False,
                            separators=(',', ': ')
                            )

        raw_data = json.dumps(request.data,
                              sort_keys=False,
                              indent=4,
                              ensure_ascii=False,
                              separators=(',', ': ')
                              )

        id = PerevalAdded.objects.last().id + 1
        serializer = PerevalAddedSerializer(data={'pkey': id, 'date_added': date_added_str, 'raw_data': raw_data, 'images': images})
        if serializer.is_valid():
            serializer = serializer.save()
            data = {"id": serializer.id}
            return Response(data=data, status=status.HTTP_200_OK)

    return Response(data='Something is wrong.', status=status.HTTP_503_SERVICE_UNAVAILABLE)
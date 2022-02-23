
from django.urls import path
from app.api.views import api_recieve_data

app_name = 'chat'

urlpatterns = [
    path('POST/pereval/', api_recieve_data, name="api_recieve_data"),
]
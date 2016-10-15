from graas.models import DataPoint
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
import pytz
import datetime

class DataPointSerializer(ModelSerializer):
    class Meta:
        model = DataPoint
        depth = 1
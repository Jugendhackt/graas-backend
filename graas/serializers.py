from graas.models import DataPoint
from rest_framework.serializers import ModelSerializer, ValidationError

import pytz
import datetime

class DataPointSerializer(ModelSerializer):
    class Meta:
        model = DataPoint
        depth = 1

    def validate_time(self, value):
        """
        Check that the date is at least one second in the future
        """
        now = datetime.datetime.now(pytz.utc)
        if now < value:
            raise ValidationError("Valid Until must be in the past")
        return value
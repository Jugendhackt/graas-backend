from graas.models import DataPoint
from graas.serializers import DataPointSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_gis.filters import InBBoxFilter
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from rest_framework_extensions.mixins import CacheResponseAndETAGMixin

import datetime
import pytz

class DefaultViewSet(viewsets.ModelViewSet):
    model_class = None
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        assert self.model_class is not None, "You need to override model_class"
        queryset = self.model_class.objects.all()
        print(queryset)
        return queryset

    def get_serializer_class(self):
        assert self.model_class is not None, "You need to override model_class"
        serializer_name = "%sSerializer" % self.model_class.__name__
        return globals()[serializer_name]

class DataPointViewSet(DefaultViewSet):
    model_class = DataPoint
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter, DjangoFilterBackend)
    permission_classes = ()
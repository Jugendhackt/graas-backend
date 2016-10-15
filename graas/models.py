from django.contrib.gis.db import models

# Create your models here.
class DataPoint(models.Model):
    location = models.PointField()
    count = models.IntegerField()
    time = models.DateTimeField()

from django.contrib.gis.db import models

# Create your models here.
class DataPoint(models.Model):
    location = models.PointField()
    uSv = models.FloatField()
    time = models.IntegerField()

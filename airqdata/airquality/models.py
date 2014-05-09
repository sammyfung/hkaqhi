from django.db import models

class AirQuality(models.Model):
  reptime = models.DateTimeField()
  stationid = models.IntegerField()
  stationcode = models.CharField(max_length=4)
  stationtype = models.CharField(max_length=32,null=True)
  name = models.CharField(max_length=32)
  aqhi = models.IntegerField(null=True)
  no2 = models.FloatField(null=True)
  o3 = models.FloatField(null=True)
  so2 = models.FloatField(null=True)
  co = models.FloatField(null=True)
  pm10 = models.FloatField(null=True)
  pm25 = models.FloatField(null=True)


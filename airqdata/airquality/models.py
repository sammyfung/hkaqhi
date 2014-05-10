from django.db import models

class AirQuality(models.Model):
  reptime = models.DateTimeField()
  stationid = models.IntegerField()
  stationcode = models.CharField(max_length=4)
  stationtype = models.CharField(max_length=32,null=True,blank=True)
  name = models.CharField(max_length=32)
  aqhi = models.IntegerField(null=True,blank=True)
  no2 = models.FloatField(null=True,blank=True)
  o3 = models.FloatField(null=True,blank=True)
  so2 = models.FloatField(null=True,blank=True)
  co = models.FloatField(null=True,blank=True)
  pm10 = models.FloatField(null=True,blank=True)
  pm25 = models.FloatField(null=True,blank=True)


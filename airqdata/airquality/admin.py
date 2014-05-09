from django.contrib import admin
from airquality.models import AirQuality

class AirQualityAdmin(admin.ModelAdmin):
     list_display = ('reptime', 'stationid', 'stationcode', 'stationtype', 'name','aqhi','no2','o3','so2','co','pm10','pm25')
     list_filter = ['stationid', 'stationtype']

admin.site.register(AirQuality, AirQualityAdmin)


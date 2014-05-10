# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from airquality.models import AirQuality

class HkaqhiPipeline(object):
    def process_item(self, item, spider):
      if spider.name == 'pollutant24':
        if AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'], stationtype__isnull = True):
          obj = AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'])
          try:
            obj.update(no2=item['no2'])
          except KeyError:
            pass
          try:
            obj.update(o3=item['o3'])
          except KeyError:
            pass
          try:
            obj.update(so2=item['so2'])
          except KeyError:
            pass
          try:
            obj.update(co=item['co'])
          except KeyError:
            pass
          try:
            obj.update(pm10=item['pm10'])
          except KeyError:
            pass
          try:
            obj.update(pm25=item['pm25'])
          except KeyError:
            pass
        elif not AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid']):
          item.save()
        else:
          raise DropItem("Pollutant data time %s from station %s exists." % (item['reptime'],item['name']))
      elif spider.name == 'aqhi24':
        if AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'], aqhi__isnull = True):
          obj = AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'])
          try:
            obj.update(stationtype=item['stationtype'])
          except KeyError:
            pass
          try:
            obj.update(aqhi=item['aqhi'])
          except KeyError:
            pass
        elif not AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid']):
          item.save()
        else:
          raise DropItem("AQHI data time %s from station %s exists." % (item['reptime'],item['name']))
      return item

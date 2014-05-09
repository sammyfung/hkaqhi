# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from airquality.models import AirQuality

class HkaqhiPipeline(object):
    def process_item(self, item, spider):
      if spider.name == 'pollutant24':
        if not AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'], aqhi__isnull = True):
          item.save()
        else:
          raise DropItem("Pollutant data time %s from station %s exists." % (item['reptime'],item['name']))
      elif spider.name == 'aqhi24':
        if not AirQuality.objects.filter(reptime = item['reptime'], stationid=item['stationid'], aqhi__isnull = False):
          item.save()
        else:
          raise DropItem("AQHI data time %s from station %s exists." % (item['reptime'],item['name']))
      return item

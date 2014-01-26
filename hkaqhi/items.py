# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class HkaqhiItem(Item):
    stationtype = Field()
    name = Field()
    time = Field()
    aqhi = Field()
    id = Field()
    stationid = Field()

class PollutantItem(Item):
    name = Field()
    id = Field()
    stationid = Field()
    time = Field()
    no2 = Field()
    o3 = Field()
    so2 = Field()
    co = Field()
    pm10 = Field()
    pm25 = Field()

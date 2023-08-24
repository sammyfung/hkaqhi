from scrapy.item import Item, Field

class HkaqhiItem(Item):
    type = Field()
    name = Field()
    time = Field()
    aqhi = Field()
    no2 = Field()
    o3 = Field()
    so2 = Field()
    co = Field()
    pm10 = Field()
    pm25 = Field()
    id = Field()
    code = Field()



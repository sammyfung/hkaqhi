from scrapy.spiders import Spider
from scrapy.selector import Selector
from hkaqhi.items import HkaqhiItem
from datetime import datetime
import re
from hkaqhi.epdstations import EPDStations


class Pollutant24Spider(Spider):
    name = "pollutant24"
    allowed_domains = ["aqhi.gov.hk"]
    tl = '%Y-%m-%d %H:%M %z'

    def __init__(self):
        self.start_urls = self.generate_url()

    def parse(self, response):
        items = []
        hxs = Selector(response)
        station_name = hxs.xpath('//div[@id="dd_stnh24_stationName"]//text()').extract()[0]
        for r in hxs.xpath('//div[@id="cltNormal"]/table/tbody/tr'):
            d = r.xpath('td/text()').extract()
            if len(d) == 7:
                item = HkaqhiItem()
                stations = EPDStations()
                item['name'] = station_name
                item['code'] = None
                item['id'] = None
                for name, code in stations.station_code:
                    item['code'] = code if name == item['name'] else item['code']
                for name, id in stations.station_id:
                    item['id'] = int(id) if name == item['name'] else item['id']
                item['time'] = datetime.strptime(re.sub('\xa0',' ',d[0] + ' +0800'), self.tl).isoformat()
                for i in range(1,7):
                    d[i] = re.sub('\,','',d[i])
                try:
                    item['no2'] = float(d[1])
                except ValueError:
                    pass
                try:
                    item['o3'] = float(d[2])
                except ValueError:
                    pass
                try:
                    item['so2'] = float(d[3])
                except ValueError:
                    pass
                try:
                    item['co'] = float(d[4])
                except ValueError:
                    pass
                try:
                    item['pm10'] = float(d[5])
                except ValueError:
                    pass
                try:
                    item['pm25'] = float(d[6])
                except ValueError:
                    pass
                items.append(item)
        return items
   
    def generate_url(self):
        stations = EPDStations()
        start_url = []
        for name, code in stations.station_code:
            start_url += [ 'http://www.aqhi.gov.hk/en/aqhi/past-24-hours-pollutant-concentration' + code + '.html' ]
        return start_url

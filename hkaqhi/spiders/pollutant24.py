from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from hkaqhi.items import AirQualityItem
from datetime import datetime
import re

class Pollutant24Spider(Spider):
    name = "pollutant24"
    allowed_domains = ["aqhi.gov.hk"]
    #start_urls = (
    #    'http://www.aqhi.gov.hk/en/aqhi/past-24-hours-pollutant-concentration.html',
    #    )
    newid = {'Central/Western': '45fd',
        'Eastern': 'e1a6',
        'Kwun Tong': 'fb71',
        'Sham Shui Po': 'db46',
        'Kwai Chung': '30e8',
        'Tsuen Wan': '228e',
        'Yuen Long': '1f2c',
        'Tuen Mun': '537c',
        'Tung Chung': 'f322',
        'Tai Po': '6e9c',
        'Sha Tin': '2c5f',
        'Tap Mun': '233a',
        'Causeway Bay': '5ca5',
        'Central': 'f9dd',
        'Mong Kok': '9c57'}
    oldid = {'Central/Western': '80',
        'Eastern': '73',
        'Kwun Tong': '74',
        'Sham Shui Po': '66',
        'Kwai Chung': '72',
        'Tsuen Wan': '77',
        'Yuen Long': '70',
        'Tuen Mun': '82',
        'Tung Chung': '78',
        'Tai Po': '69',
        'Sha Tin': '75',
        'Tap Mun': '76',
        'Causeway Bay': '71',
        'Central': '79',
        'Mong Kok': '81'}
    tl = '%Y-%m-%d %H:%M'

    def __init__(self):
        self.start_urls = self.generate_url()

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        name = hxs.select('//div[@class="tilNormal"]//text()').extract()[0]
        for r in hxs.select('//div[@id="cltNormal"]/table/tbody/tr'):
            d = r.select('td/text()').extract()
            if len(d) == 7:
                item = AirQualityItem()
                item['name'] = name
                item['stationcode'] = self.newid[name]
                item['stationid'] = self.oldid[name]
	            item['reptime'] = datetime.strptime(re.sub('\xa0',' ',d[0]), self.tl)
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
        start_url = []
        for i in self.newid.values():
            start_url += [ 'http://www.aqhi.gov.hk/en/aqhi/past-24-hours-pollutant-concentration'+i+'.html' ]
        return start_url

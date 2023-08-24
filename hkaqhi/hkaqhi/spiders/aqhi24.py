from scrapy.spiders import XMLFeedSpider
from hkaqhi.items import HkaqhiItem
from datetime import datetime
from hkaqhi.epdstations import EPDStations

class Aqhi24Spider(XMLFeedSpider):
    name = 'aqhi24'
    allowed_domains = ['aqhi.gov.hk']
    start_urls = ['http://www.aqhi.gov.hk/epd/ddata/html/out/24aqhi_Eng.xml']
    itertag = 'item'
    tl = '%a, %d %b %Y %X %z'

    def parse_node(self, response, node):
        i = HkaqhiItem()
        stations = EPDStations()
        station_type = node.xpath('type/text()').extract()[0]
        if station_type == 'General Stations':
            i['type'] = 'General'
        elif station_type == 'Roadside Stations':
            i['type'] = 'Roadside'
        else:
            i['type'] = 'Unknown'
        i['name'] = node.xpath('StationName/text()').extract()[0]
        i['time'] = datetime.strptime(node.xpath('DateTime/text()').extract()[0], self.tl).isoformat()
        try:
          i['aqhi'] = int(node.xpath('aqhi/text()').extract()[0])
        except ValueError:
          if node.xpath('aqhi/text()').extract()[0] == "10+":
            i['aqhi'] = 11
        i['code'] = None
        i['id'] = None
        for name, code in stations.station_code:
            i['code'] = code if name == i['name'] else i['code']
        for name, id in stations.station_id:
            i['id'] = int(id) if name == i['name'] else i['id']
        return i

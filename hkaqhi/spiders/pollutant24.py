from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class Pollutant24Spider(BaseSpider):
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

    def __init__(self):
        self.start_urls = self.generate_url()

    def parse(self, response):
        pass
   
    def generate_url(self):
        start_url = []
        for i in self.newid.values():
            start_url += [ 'http://www.aqhi.gov.hk/en/aqhi/past-24-hours-pollutant-concentration'+i+'.html' ]
        return start_url

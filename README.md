hkaqhi
======

This is a open source project to scrap past 24 hours of Hong Kong Air Quality 
Health Index (AQHI) from Data.One dataset, convert from XML data to JSON 
format.

This project is written in python with scrapy.

Data.One - http://www.gov.hk/en/theme/psi/datasets/ 

Installation Example
--------------------

$ virtualenv hkaqhi  
$ source hkaqhi/bin/activate  
$ pip install scrapy  
$ git clone https://github.com/sammyfung/hkaqhi.git  
$ cd hkaqhi  

To crawl past 24 hours of AQHI:
$ scrapy crawl aqhi24 -t json -o aqhi24.json  

To crawl past 24 hours of detailed pollutant concentration data:
$ scrapy crawl pollutant24 -t json -o ~/pollutant24.json

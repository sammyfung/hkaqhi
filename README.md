hkaqhi
======

This is a open source project to scrap past 24 hours of Hong Kong Air Quality 
Health Index (AQHI) from Data.One dataset, convert from XML data to JSON 
format.

This project is written in python with scrapy and django.

Data.One - http://www.gov.hk/en/theme/psi/datasets/ 

Installation Example
--------------------

Setup Python Enviornement and Cloning this project   
$ virtualenv env  
$ source env/bin/activate  
$ git clone https://github.com/sammyfung/hkaqhi.git  
$ cd hkaqhi  
$ pip install -r requirements.txt   

Initial Django Database   
$ cd airqdata   
$ python manage.py syncdb   

To crawl past 24 hours of AQHI with output file in json format:  
$ scrapy crawl aqhi24 -t json -o aqhi24.json  

To crawl past 24 hours of detailed pollutant concentration data with output file in json format:  
$ scrapy crawl pollutant24 -t json -o ~/pollutant24.json

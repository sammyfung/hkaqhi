hkaqhi
======

Developer: Sammy Fung <sammy@sammy.hk>

This is a open source project to scrap past 24 hours of Hong Kong Air Quality 
Health Index (AQHI) from Data.One dataset, convert from XML data to JSON 
format.

This project is written in python with scrapy and django.

DATA.GOV.HK (by OGCIO) - https://data.gov.hk/en   
Hong Kong Air Quality Health Index (by Environement Protection Department EPD) - http://www.aqhi.gov.hk/en.html   

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
$ python manage.py makemigrations
$ python manage.py syncdb   

Crawling
--------

To crawl past 24 hours of AQHI with output file in json format:  
$ scrapy crawl aqhi24 -t json -o aqhi24.json  

To crawl past 24 hours of detailed pollutant concentration data with output file in json format:  
$ scrapy crawl pollutant24 -t json -o ~/pollutant24.json

JSON API
--------

Optional Params:   
id = station id (default: past hour data of all stations)   
start = start time (default: past 1/24-hour data of all/single stations)  

Example: http://localhost:8000/airquality/station/?start=20150525&id=82  

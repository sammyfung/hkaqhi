[![hkaqhi](https://github.com/sammyfung/hkaqhi/actions/workflows/hkaqhi.yml/badge.svg)](https://github.com/sammyfung/hkaqhi/actions/workflows/hkaqhi.yml) [![codecov](https://codecov.io/gh/sammyfung/hkaqhi/graph/badge.svg?token=G5DVA9F2LH)](https://codecov.io/gh/sammyfung/hkaqhi)

hkaqhi
======

hkaqhi scrapes the past 24 hours of Air Quality and pollutant concentration data from Hong Kong [Air Quality Health Index](https://www.aqhi.gov.hk/en.html) (AQHI) website by Environment Protection Department (EPD).

Installation
------------

Cloning the project and setup a python virtual enviornment to install required package.
```
$ git clone git@github.com:sammyfung/hkaqhi.git
$ cd hkaqhi
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip install -r requirements.txt   
```
Quickstart
--------

To crawl past 24 hours of AQHI and append to an output file in json format:
```
$ scrapy crawl aqhi24 -o aqhi24.json  
```

To crawl past 24 hours of detailed pollutant concentration data and append to an output file in json format:  
```
$ scrapy crawl pollutant24 -o pollutant24.json
```

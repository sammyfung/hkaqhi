# Scrapy settings for hkaqhi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hkaqhi'

SPIDER_MODULES = ['hkaqhi.spiders']
NEWSPIDER_MODULE = 'hkaqhi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hkaqhi (+http://www.yourdomain.com)'

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","airqdata.settings")
path = os.path.join(os.path.dirname(__file__),'../airqdata')
sys.path.append(os.path.abspath(path))
from django.conf import settings
import django
django.setup()

ITEM_PIPELINES = {
  'hkaqhi.pipelines.HkaqhiPipeline': 300,
}



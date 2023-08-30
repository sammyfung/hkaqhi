# Scrapy settings for hkaqhi project
BOT_NAME = 'hkaqhi'

SPIDER_MODULES = ['hkaqhi.spiders']
NEWSPIDER_MODULE = 'hkaqhi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hkaqhi (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'hkaqhi.pipelines.HkaqhiPipeline': 300,
}



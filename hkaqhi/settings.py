# Scrapy settings for hkaqhi project
BOT_NAME = 'hkaqhi'

SPIDER_MODULES = ['hkaqhi.spiders']
NEWSPIDER_MODULE = 'hkaqhi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hkaqhi (+http://www.yourdomain.com)'

# Initialize Django web framework for data store
# Use environment variable PYTHONPATH for abspath to Django project
# and DJANGO_SETTINGS_MODULE for Settings filename of Django project
try:
    import django
    django.setup()
except ImportError:
    # Allow to work without Django
    pass

ITEM_PIPELINES = {
    'hkaqhi.pipelines.HkaqhiPipeline': 300,
}



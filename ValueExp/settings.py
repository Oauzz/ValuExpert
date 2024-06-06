# Scrapy settings for ValueExp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging

LOG_LEVEL = logging.INFO
BOT_NAME = "ValueExp"

SPIDER_MODULES = ["ValueExp.spiders"]
NEWSPIDER_MODULE = "ValueExp.spiders"

DOWNLOAD_DELAY = 2  # 3 seconds delay

# Randomize download delay to avoid detection
RANDOMIZE_DOWNLOAD_DELAY = True

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2  # initial download delay
AUTOTHROTTLE_MAX_DELAY = 60  # maximum download delay to be set in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # average number of requests Scrapy should be sending in parallel to each remote server

# RETRY_ENABLED = True
# RETRY_TIMES = 2  # Number of retries
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # Retry on these HTTP codes
HTTPERROR_ALLOWED_CODES = [512,511,429]
# DOWNLOAD_DELAY = 2

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False


# Add MongoDB connection settings
MONGO_URI = 'mongodb+srv://ouzamapro:ouzamapro@valuexpert.j6zwfb1.mongodb.net/'
MONGO_DB_RENT = 'rent_db'
MONGO_DB_SELL = 'sell_db'

# Enable MongoDB pipeline
ITEM_PIPELINES = {
    'ValueExp.pipelines.ValueexpPipeline': 300,
}


SCRAPEOPS_API_KEY = 'f81d2bb0-e6b2-4757-ab69-b2fed05dab00'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True 
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5
SCRAPEOPS_RESIDENTIAL = 'true'


PROXY_USER = 'spckd6fg5g'
PROXY_PASSWORD = 'lz89wpSlpNi0z3aFN_'
PROXY_ENDPOINT = 'ma.smartproxy.com'
PROXY_PORT = '40001'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ValueExp (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "ValueExp.middlewares.ValueexpSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #  'ValueExp.middlewares.ScrapeOpsProxyMiddleware': 543,
   # "ValueExp.middlewares.ValueexpDownloaderMiddleware": 543,
   # 'ValueExp.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
   'ValueExp.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
   # 'ValueExp.middlewares.MyProxyMiddleware': 350, 
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "ValueExp.pipelines.ValueexpPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

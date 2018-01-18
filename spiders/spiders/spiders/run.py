import os


#run all spiders
os.system('scrapy crawl wp_spider')
os.system('scrapy crawl npr_spider')
os.system('scrapy crawl politico_spider')
os.system('scrapy crawl econ_spider')
os.system('scrapy crawl nyt_spider')
os.system('scrapy crawl wsj_spider')
os.system('scrapy crawl bbc_spider')


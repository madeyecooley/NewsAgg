#run.py

import os
from delete_db import deletedb
from populate_db import populatedb


#delete database
deletedb()

#run all spiders
os.system('scrapy crawl wp_spider')
os.system('scrapy crawl npr_spider')
os.system('scrapy crawl politico_spider')
os.system('scrapy crawl econ_spider')
os.system('scrapy crawl nyt_spider')
os.system('scrapy crawl wsj_spider')
os.system('scrapy crawl bbc_spider')


#populate database
populatedb()

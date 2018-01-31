#run.py

import os
from delete_db import deletedb
from populate_db import populatedb

def delete_dbfile(filename):
    with open(filename, "w") as myfile:
        pass
    myfile.close()


#delete database
deletedb()

#delete db_data.txt file
#os.system("> db_data.txt")
#delete_dbfile("db_data.txt")


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

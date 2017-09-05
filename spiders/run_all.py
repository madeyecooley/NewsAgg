from scrapy.crawler import CrawlerProcess

from spiders.spiders.bbc_spider import BBCSpider
from spiders.spiders.thall_spider import THALLSpider
from spiders.spiders.theecon_spider import ECONSpider
from spiders.spiders.wsj_spider import WSJSpider
from spiders.spiders.wp_spider import WPSpider
from spiders.spiders.politico_spider import PoliticoSpider
from spiders.spiders.nyt_spider import NYTSpider
from spiders.spiders.npr_spider import NPRSpider
from spiders.spiders.natrev_spider import NatRevSpider


# This script runs all of the spiders and hopefully populates a database with the output


spider1 = NatRevSpider(domain='www.nationalreview.com')
spider2 = NPRSpider(domain='www.npr.org')
spider3 = NYTSpider(domain='www.nytimes.com')
spider4 = PoliticoSpider(domain='www.politico.com')
spider5 = WPSpider(domain='www.washingtonpost.com')
spider6 = WSJSpider(domain='www.wsj.com')
spider7 = ECONSpider(domain='www.economist.com')
spider8 = THALLSpider(domain='www.townhall.com')
spider9 = BBCSpider(domain='www.bbc.com')

crawler = CrawlerProcess()
crawler.crawl(spider1)
crawler.crawl(spider2)
crawler.crawl(spider3)
crawler.crawl(spider4)
crawler.crawl(spider5)
crawler.crawl(spider6)
crawler.crawl(spider7)
crawler.crawl(spider8)
crawler.crawl(spider9)

crawler.start()
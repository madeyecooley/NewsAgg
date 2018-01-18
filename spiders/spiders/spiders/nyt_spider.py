from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor
#from .populate_db import add_to_db

class NYTSpider(Spider):
    name = 'nyt_spider'
    allowed_domains = ['www.nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage']

    rules = (
        Rule(LinkExtractor(allow="http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage"), callback='parse'),
    )

    def parse(self, response):
        items = []
        for div in response.xpath('//*[@class="aColumn"]/div[1]/div'):
            item = Article()
            item["Title"] = div.xpath('h3/a/text()').extract()[0]
            item["URL"] = div.xpath('h3/a/@href').extract()[0]
            item["Summary"] = div.xpath('p[@class="summary"]/text()').extract()[0]
            item["Photo"] = div.xpath('div/a/img/@src').extract()[0]
            item["Site"] = "New York Times"

            items.append(item)

            #get_article(item["URL"])

            if item["Title"] != "":
                title = item["Title"]
                title = title.encode('utf-8').strip()
            else:
                title = ""

            if item["Summary"] != "":
                summary = item["Summary"]
                summary = summary.encode('utf-8').strip()
            else:
                summary = ""

            if item["Photo"] != "":
                imgsrc = item["Photo"]
                imgsrc = imgsrc.encode('utf-8').strip()
            else:
                imgsrc = ""

            if item["URL"] != "":
                url = item["URL"]
                url = url.encode('utf-8').strip()
            else:
                url = ""

            if item["Site"] != "":
                site = item["Site"]
            else:
                site = ""

            #add_to_db(title, summary, "",  url, site)

            with open("db_data.txt", "a") as myfile:
                myfile.write('\t')
                myfile.write(title)
                myfile.write('\t')
                myfile.write(summary)
                myfile.write('\t')
                myfile.write(imgsrc)
                myfile.write('\t')
                myfile.write(url)
                myfile.write('\t')
                myfile.write(site)
                myfile.write('\n')












            



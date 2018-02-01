from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from .get_article import get_article
from scrapy.linkextractors import LinkExtractor

class NPRSpider(Spider):
    name = 'npr_spider'
    allowed_domains = ['www.npr.org']
    start_urls = ['http://www.npr.org/sections/news/archive']

    rules = (
        Rule(LinkExtractor(allow="http://www.npr.org/sections/news/archive"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@id="archive-core"]/div/article'):
            item = Article()
            item["Title"] = article.xpath('div/h2[@class="title"]/a/text()').extract()[0]
            item["URL"] = article.xpath('div/h2[@class="title"]/a/@href').extract()[0]
            item["Summary"] = article.xpath('div/p[@class="teaser"]/a/text()').extract()[0]
            if article.xpath('@class').extract()[0] != "item no-image":
            	item["Photo"] = article.xpath('div/div/a/img/@src').extract()[0]
            else:
                item["Photo"] = ""
            item["Site"] = "NPR"

            items.append(item)
            
            text = get_article(item["URL"]).encode('utf-8').strip()
            text = text.replace('\n', ' ')
	
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
                myfile.write('\t')
                myfile.write(text)
                myfile.write('\n')
 
            myfile.close()

from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class ECONSpider(Spider):
    name = 'econ_spider'
    allowed_domains = ['www.economist.com']
    start_urls = ['https://www.economist.com/latest-updates']

    rules = (
        Rule(LinkExtractor(allow="https://www.economist.com/latest-updates"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@class="main-content__teaser-list '
                                      'main-content__teaser-list--blog-page '
                                      'main-content__main-column"]/div[1]/article'):
            if article.xpath('a/div[2]/h3/span[1]/text()').extract()[0] != "Indicators": 
                item = Article()
                item["Title"] = article.xpath('a/div/h3/span[2]/text()').extract()[0]
                item["URL"] = article.xpath('a/@href').extract()[0]
                item["URL"] = "https://www.economist.com" + item["URL"]
                item["Summary"] = article.xpath('a/div[2]/div[1]/text()').extract()[0]
                item["Photo"] = article.xpath('a/div[1]/div/div/div/img/@src').extract()
                item["Site"] = "The Economist"

                items.append(item)
                print_item(item)
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

            #if item["Photo"] != "":
            #    imgsrc = item["Photo"]
            #    imgsrc = imgsrc.encode('utf-8').strip()
            #else:
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
                myfile.write('\n')


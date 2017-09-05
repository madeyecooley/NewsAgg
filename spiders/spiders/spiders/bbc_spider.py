from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class BBCSpider(Spider):
    name = 'bbc_spider'
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/news']

    rules = (
        Rule(LinkExtractor(allow="http://www.bbc.com/news"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@class="nw-c-most-read__items gel-layout '
                                      'gel-layout--no-flex"]/ol/li'):
            item = Article()
            item["Title"] = article.xpath('span/div/a/span/text()').extract()[0]
            temp = article.xpath('span/div/a/@href').extract()[0]
            item["URL"] = ''.join("http://www.bbc.com" + str(temp))
            # item["Summary"] = article.xpath('article/div/header/p[2]/text()').extract()[0]
            # item["Photo"] = article.xpath('article/figure/a/img/@src').extract()[0]
            item["Site"] = "BBC News"

            items.append(item)
            print_item(item)
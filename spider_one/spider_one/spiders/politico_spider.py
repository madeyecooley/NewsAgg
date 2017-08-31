from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class PoliticoSpider(Spider):
    name = 'politico_spider'
    allowed_domains = ['www.politico.com']
    start_urls = ['http://www.politico.com/magazine/story']

    rules = (
        Rule(LinkExtractor(allow="http://www.politico.com/magazine/story"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@class="content-group web-archive-results"]/ul/li'):
            item = Article()
            item["Title"] = article.xpath('article/div/header/h3/a/text()').extract()[0]
            item["URL"] = article.xpath('article/div/header/h3/a/@href').extract()[0]
            item["Summary"] = article.xpath('article/div/header/p[2]/text()').extract()[0]
            item["Photo"] = article.xpath('article/figure/a/img/@src').extract()[0]
            item["Site"] = "Politico"

            items.append(item)
            print_item(item)
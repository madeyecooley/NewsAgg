from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class WPSpider(Spider):
    name = 'wp_spider'
    allowed_domains = ['www.washingtonpost.com']
    start_urls = ['https://www.washingtonpost.com/?reload=true']

    rules = (
        Rule(LinkExtractor(allow="https://www.washingtonpost.com/?reload=true"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@class="chain-content no-skin"]/div'):
            item = Article()
            item["Title"] = article.xpath('div/div/div/div[2]/div[1]/a/text()').extract()[0]
            # item["URL"] = article.xpath('article/div/header/h3/a/@href').extract()[0]
            # item["Summary"] = article.xpath('article/div/header/p[2]/text()').extract()[0]
            # item["Photo"] = article.xpath('article/figure/a/img/@src').extract()[0]
            item["Site"] = "The Washington Post"

            items.append(item)
            print_item(item)


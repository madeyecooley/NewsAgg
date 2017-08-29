from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class NPRSpider(Spider):
    name = 'theecon_spider'
    allowed_domains = ['www.economist.com']
    start_urls = ['https://www.economist.com/latest-updates']

    rules = (
        Rule(LinkExtractor(allow="https://www.economist.com/latest-updates"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[class="teaser-list"]/article'):
            item = Article()
            item["Title"] = article.xpath('a/div[@class="teaser__group-text"]/h3/span['
                                          '@class="flytitle-and-title__title"]/text()').extract()[0]
            # item["URL"] = article.xpath('div/h2[@class="title"]/a/@href').extract()[0]
            # item["Summary"] = article.xpath('div/p[@class="teaser"]/a/text()').extract()[0]
            # item["Photo"] = article.xpath('div/div/a/img/@src').extract()
            # item["Credit_Caption"] = article.xpath('div/div[@class="credit-caption"]/span/text('
            #                                        ')').extract()
            item["Site"] = "The Economist"

            items.append(item)
            print_item(item)

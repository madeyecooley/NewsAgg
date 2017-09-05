from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class THALLSpider(Spider):
    name = 'thall_spider'
    allowed_domains = ['www.townhall.com']
    start_urls = ['https://townhall.com/tipsheet/']

    rules = (
        Rule(LinkExtractor(allow="https://townhall.com/tipsheet/"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@id="index-list"]/div'):
            item = Article()

            item["Title"] = article.xpath('div/div[2]/div[1]/a/text()').extract()[0]
            temp = article.xpath('div/div[2]/div[1]/a/@href').extract()[0]
            item["URL"] = ''.join('https://townhall.com' + str(temp))
            # item["Summary"] = article.xpath('a/article/section[@class="excerpt amt-10 '
            #                                     'serif"]/text()').extract()[0]
            item["Photo"] = article.xpath('div/div[1]/a/img/@data-src').extract()[0]
            item["Site"] = "Townhall"

            items.append(item)
            print_item(item)
from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class WSJSpider(Spider):
    name = 'wsj_spider'
    allowed_domains = ['www.wsj.com']
    start_urls = ['https://www.wsj.com/news/whats-news']

    rules = (
        Rule(LinkExtractor(allow="https://www.wsj.com/news/whats-news"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for article in response.xpath('//*[@class="module automated-news"]/ul/li'):
            item = Article()
            item["Title"] = article.xpath('div/div/h3/a/text()').extract()[0]
            item["URL"] = article.xpath('div/div/h3/a/@href').extract()[0]
            item["Summary"] = article.xpath('div/div/div/p/text()').extract()[0]
            item["Photo"] = article.xpath('div/a/img/@data-src').extract()[0]
            item["Site"] = "The Wall Street Journal"

            items.append(item)
            print_item(item)

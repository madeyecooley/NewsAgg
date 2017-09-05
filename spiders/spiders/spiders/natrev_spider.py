from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class NatRevSpider(Spider):
    name = 'natrev_spider'
    allowed_domains = ['www.nationalreview.com']
    start_urls = ['http://www.nationalreview.com/archives']

    rules = (
        Rule(LinkExtractor(allow="http://www.nationalreview.com/archives"), callback='parse'),
    )

    def parse(self, response):
        items = []

        for ul in response.xpath('//*[@class=" timeline blog cf p-r"]/ul'):
            for article in response.xpath('//*[@class=" timeline blog cf p-r"]/ul/li'):
                item = Article()

                item["Title"] = article.xpath('a/article/header/h1/text()').extract()[0]
                temp = article.xpath('a/@href').extract()[0]
                item["URL"] = ''.join("http://www.nationalreview.com" + str(temp))
                item["Summary"] = article.xpath('a/article/section[@class="excerpt amt-10 '
                                                'serif"]/text()').extract()[0]
                item["Photo"] = article.xpath('a/article/div/@style').extract()
                item["Site"] = "National Review"

                items.append(item)
                print_item(item)
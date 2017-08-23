from scrapy.spiders import Rule, Spider
from ..items import Article
from scrapy.linkextractors import LinkExtractor


def print_item(item):
    print "TITLES: %s" % item.get('Title')
    print "URLS: %s" % item.get('URL')
    print "SUMMARY: %s" % item.get('Summary')
    print "IMG URL: %s" % item.get('Photo')
    print "IMG CAPTION: %s" % item.get('Credit_Caption')
    print "ARTICLE SITE: %s" % item.get('Credit_Caption')


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
            item["Photo"] = article.xpath('div/div/a/img/@src').extract()
            item["Credit_Caption"] = article.xpath('div/div[@class="credit-caption"]/span/text('
                                                   ')').extract()
            item["Site"] = "NPR"

            items.append(item)
            # print_item(item)

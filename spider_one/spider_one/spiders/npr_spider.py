from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from ..items import NPRSpiderItem


class NPRSpider(BaseSpider):
    name = 'npr_spider'
    allowed_domains = ['www.npr.org']
    start_urls = ['http://www.npr.org/sections/news/archive']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//title/text()').extract()
        items = []

        for title in titles:
            items = NPRSpiderItem()
            items["title"] = title.select("a/text()").extract()
            items["url"] = title.select("a/@href").extract()

        print "ITEMS %s\n" % items
        return items

from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor


class NPRSpider(Spider):
    name = 'nyt_spider'
    allowed_domains = ['www.nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage']

    rules = (
        Rule(LinkExtractor(allow="http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage"), callback='parse'),
    )

    def parse(self, response):
        items = []
        for div in response.xpath('//*[@class="aColumn"]/div[1]/div'):
            item = Article()
            item["Title"] = div.xpath('h3/a/text()').extract()[0]
            item["URL"] = div.xpath('h3/a/@href').extract()[0]
            item["Summary"] = div.xpath('p[@class="summary"]/text()').extract()[0]
            item["Photo"] = div.xpath('div/a/img/@src').extract()
            item["Site"] = "NYT"

            items.append(item)
            # print_item(item)

#This section is for the smaller titles at the bottom of the site
        # for div in response.xpath('//*[@class="aColumn"]/div[2]/ul/li'):
        #     item = Article()
        #     item["Title"] = div.xpath('h6/a/text()').extract()[0]
        #     item["URL"] = div.xpath('h3/a/@href').extract()[0]
        #     # item["Summary"] = div.xpath('p[@class="summary"]/text()').extract()[0]
        #     # item["Photo"] = div.xpath('div/a/img/@src').extract()
        #     item["Site"] = "NYT"
        #
        #     items.append(item)
        #     print_item(item)


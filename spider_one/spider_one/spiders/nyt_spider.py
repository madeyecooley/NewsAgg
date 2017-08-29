from scrapy.spiders import Rule, Spider
from ..items import Article
from scrapy.linkextractors import LinkExtractor


def print_item(item):
    print "TITLES: %s" % item.get('Title')
    print "URLS: %s" % item.get('URL')
    print "SUMMARY: %s" % item.get('Summary')
    print "IMG URL: %s" % item.get('Photo')
    print "IMG CAPTION: %s" % item.get('Credit_Caption')
    print "ARTICLE SITE: %s" % item.get('Site')


class NPRSpider(Spider):
    name = 'nyt_spider'
    allowed_domains = ['www.nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage']

    rules = (
        Rule(LinkExtractor(allow="http://www.nytimes.com/pages/todayspaper/index.html?action=Click&module=HPMiniNav&region=TopBar&WT.nav=page&contentCollection=TodaysPaper&pgtype=Homepage"), callback='parse'),
    )

    def parse(self, response):
        items = []
        for div in response.xpath('//*[@id="main"]/div[2]/div/div[1]/div[2]/div['
                                      '@class="columnGroup first"]'):
            item = Article()
            item["Title"] = div.xpath('div[@class="story"]/h3/a/text()').extract()[0]
            # item["URL"] = article.xpath('div[@class="story"]/h3/a/@href').extract()[0]
            # item["Summary"] = article.xpath('div/p[@class="summary"]/text()').extract()[0]
            # item["Photo"] = article.xpath('div[@class="thumbnail"]/a/img/@src').extract()
            # # item["Credit_Caption"] = article.xpath('div/div[@class="credit-caption"]/span/text('
            # #                                        ')').extract()
            item["Site"] = "NYT"

            items.append(item)
            print_item(item)
# //*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]
# //*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]/div[1]/h3/a
# //*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]/div[2]/h3/a
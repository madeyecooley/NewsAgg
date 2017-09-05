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

        for article in response.xpath('//*[@class="chain-content no-skin "]/div[not(preceding-sibling::wp-ad)]'):
            item = Article()
            # x = article.xpath('wp-ad/text()').extract[0]
            #
            # if not x:
            #     print "TRUE"

            item["Title"] = article.xpath('div/div/div/div/div/a['
                                          '@data-pb-field="web_headline"]/text()').extract()
            item["URL"] = article.xpath('div/div/div/div/div/a['
                                          '@data-pb-field="web_headline"]/@href').extract()
            item["Summary"] = article.xpath('div/div/div/div[2]/div[@class="blurb normal '
                                            'normal-style "]/text()').extract()
            item["Photo"] = article.xpath('/div/div/div/div[1]/div/div[1]/a/img/@src').extract()
            item["Site"] = "The Washington Post"

            items.append(item)
            print_item(item)
# //*[@id="fXcWds1SFmwnuq"]/div/div/div/div[2]/div[2]
# //*[@id="fXcWds1SFmwnuq"]/div/div/div/div[1]/div/div[1]/a/img
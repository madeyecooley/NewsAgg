from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor
from .get_article import get_article

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

            if item["Title"] != "":
                title = item["Title"]
                title = title.encode('utf-8').strip()
            else:
                title = ""

            if item["Summary"] != "":
                summary = item["Summary"]
                summary = summary.encode('utf-8').strip()
            else:
                summary = ""

            if item["Photo"] != "":
                imgsrc = item["Photo"]
                imgsrc = imgsrc.encode('utf-8').strip()
            else:
                imgsrc = ""

            if item["URL"] != "":
                url = item["URL"]
                url = url.encode('utf-8').strip()
            else:
                url = ""

            if item["Site"] != "":
                site = item["Site"]
            else:
                site = ""

            text = get_article(item["URL"]).encode('utf-8').strip()
            text = text.replace('\n', ' ')

            with open("db_data.txt", "a") as myfile:
                myfile.write('\t')
                myfile.write(title)
                myfile.write('\t')
                myfile.write(summary)
                myfile.write('\t')
                myfile.write(imgsrc)
                myfile.write('\t')
                myfile.write(url)
                myfile.write('\t')
                myfile.write(site)
                myfile.write('\t')
                myfile.write(text)
                myfile.write('\n')

            myfile.close()

from scrapy.spiders import Rule, Spider
from ..items import Article
from .misc_functions import print_item
from scrapy.linkextractors import LinkExtractor
from .get_article import get_article

class WPSpider(Spider):
    name = 'wp_spider'
    allowed_domains = ['www.washingtonpost.com']
    #start_urls = ['https://www.washingtonpost.com/?reload=true']
    start_urls = ['https://www.washingtonpost.com/politics/?nid=top_nav_politics&utm_term=.0723bbdfdbfb']

    #rules = (
    #    Rule(LinkExtractor(allow="https://www.washingtonpost.com/?reload=true"), callback='parse'),
    #)

    rules = (
        Rule(LinkExtractor(allow="https://www.washingtonpost.com/politics/?nid=top_nav_politics&utm_term=.0723bbdfdbfb"), callback='parse'),
    )


    def parse(self, response):
        items = []
        artnum = 0  #this counts the number of articles
        for div in response.xpath('//*[@id="fF6Zmc2WChZaBq"]/div/div[1]/div[1]/div'):
            item = Article()
            item["Title"] = div.xpath('div[1]/div[1]/h3/a/text()').extract()[0]
            item["URL"] = div.xpath('div[1]/div[1]/h3/a/@href').extract()[0]
            item["Summary"] = div.xpath('div[1]/div[2]/p/text()').extract()[0]
            item["Photo"] = div.xpath('div[2]/a/img/@data-hi-res-src').extract()[0]
            item["Site"] = "The Washington Post"

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

            #add_to_db(title, summary, "",  url, site)

            # 'w+' overwrites contents of the file since this spider is
            # the first spider that is ran

            text = get_article(item["URL"]).encode('utf-8').strip()
            text = text.replace('\n', ' ') 

            if artnum == 0:
                with open("db_data.txt", "w+") as myfile:
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
            else:
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


            artnum += 1

            myfile.close

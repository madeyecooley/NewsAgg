#import requests
import urllib
from bs4 import BeautifulSoup

""" this function visits the link to the article and extracts the article text
    For more on requests:
    http://docs.python-requests.org/en/master/user/quickstart/ 
    http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html """

def get_article(url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    type(soup)
    print soup.prettify()[0:1000]

    
    title = url + '.txt'
    #f = open('hello.txt', 'w')

    
    #f.write(article.encode('utf-8'))
    #f.close()

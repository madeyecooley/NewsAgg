News Aggregator
===============
This is a website that aggregates daily news articles from multiple news sites to one place.
This project is still in progress.

Scrapy must be installed in order to run the spiders.

https://doc.scrapy.org/en/latest/intro/install.html

How to run spiders:

Individual Spider:

1. cd /NewsAgg/spiders/spiders/spiders

2. scrapy crawl npr_spider

All Spiders:

1. cd /NewsAgg/spiders

2. python run_all.py OR in /NewsAgg/spiders/spiders 'python run.py'

run.py creates a text file with all of the information from each news site. The information includes:
article title, article url, photo url, summary, and which news site the article came from.


How to run Django app:

1. cd /NewsAgg

2. python manage.py makemigrations  //to apply migrations to database

3. python manage.py migrate  //creates the datastructure

4. python manage.py runserver 127.0.0.1:8000

5. To view the articles home page go to 127.0.0.1:8000/articles


About this application:

- Uses mariadb as the database

- spiders are written in python



For tabs in html
http://inspirationalpixels.com/tutorials/creating-tabs-with-html-css-and-jquery

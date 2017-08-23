from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_author = models.CharField(max_length=250)
    article_summary = models.CharField(max_length=1000)
    article_photo = models.CharField(max_length=1000)
    article_url = models.CharField(max_length=300)
    article_site = models.CharField(max_length=50) #i.e NPR, Fox News, etc

    def __str__(self):
        return self.article_title + ' - ' + self.article_author

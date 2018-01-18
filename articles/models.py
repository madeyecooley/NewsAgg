from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_summary = models.CharField(max_length=2000)
    article_photosrc = models.URLField(max_length=300)
    article_url = models.URLField(max_length=300)
    article_site = models.CharField(max_length=50) #i.e NPR, Fox News, etc

    def __str__(self):
        return self.article_title + ' - ' + self.article_summary

    def __unicode__(self):
        return self.article_title

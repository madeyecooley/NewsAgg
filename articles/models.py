from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_summary = models.CharField(max_length=1000)
    article_photo = models.CharField(max_length=1000)
    article_photosrc = models.URLField(max_length=300, default="DEFAULT VALUE")
    article_url = models.URLField()
    article_site = models.CharField(max_length=50, default="") #i.e NPR, Fox News, etc

    def __str__(self):
        return self.article_title + ' - ' + self.article_summary

    def __unicode__(self):
        return self.article_title

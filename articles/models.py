from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_author = models.CharField(max_length=250)
    article_subtitle = models.CharField(max_length=1000)
    article_coverphoto = models.CharField(max_length=1000)
    article_url = models.CharField(max_length=300)

    def __str__(self):
        return self.article_title + ' - ' + self.article_author

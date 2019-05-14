from django.db import models
from django.conf import settings


class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    page_url = models.CharField(max_length=500, default='https://university.innopolis.ru/en/')

    def publish(self):
        self.save()


class URL(models.Model):
    site_url = models.CharField(max_length=500)
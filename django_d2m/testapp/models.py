from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    read = models.IntegerField(default=0)

    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)

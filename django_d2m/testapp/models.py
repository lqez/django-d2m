from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    read = models.IntegerField(default=0)

    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

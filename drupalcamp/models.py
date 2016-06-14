from __future__ import unicode_literals

from django.db import models

from datetime import datetime

class BaseAbstractModel(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    deleted = models.BooleanField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Type(BaseAbstractModel):
    name = models.CharField(max_length=200)
    iconURL = models.URLField(blank=True, null=True)


class Level(BaseAbstractModel):
    name = models.CharField(max_length=200)


class Track(BaseAbstractModel):
    name = models.CharField(max_length=200)


class Speaker(BaseAbstractModel):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    characteristic = models.TextField()
    jobTitle = models.CharField(max_length=200)
    organizationName = models.CharField(max_length=200)
    twitterName = models.CharField(max_length=200, blank=True, null=True)
    webSite = models.CharField(max_length=200, blank=True, null=True)
    avatarImageURL = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Location(BaseAbstractModel):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class POI(BaseAbstractModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    imageURL = models.URLField(blank=True, null=True)
    detailURL = models.URLField(blank=True, null=True)


class Event(BaseAbstractModel):
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    text = models.TextField()
    version = models.CharField(max_length=200)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, blank=True, null=True)
    experienceLevel = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True, null=True)
    track = models.ForeignKey('Track', on_delete=models.CASCADE, blank=True, null=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True


class Session(Event):
    def __str__(self):
        return self.name


class BoF(Event):
    def __str__(self):
        return self.name


class SocialEvent(Event):
    def __str__(self):
        return self.name


class Page(BaseAbstractModel):
    title = models.CharField(max_length=200)
    html = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class FloorPlan(BaseAbstractModel):
    name = models.CharField(max_length=200)
    imageURL = models.URLField(blank=True, null=True)



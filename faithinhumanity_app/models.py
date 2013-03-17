from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms

import datetime
import os

class Base(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True

class Tweet(Base):
    id_str            = models.CharField(unique=True, max_length=255)
    is_good           = models.NullBooleanField(blank=True, null=True)
    text              = models.CharField(max_length=255)
    username          = models.CharField(max_length=255)
    screenname        = models.CharField(max_length=255)
    profile_image_url = models.URLField(max_length=255)

    def __unicode__(self):
        return u'@%s: %s [%s]' % (self.screenname, self.text, "GOOD" if self.is_good else "BAD" if self.is_good is False else "UNSURE")

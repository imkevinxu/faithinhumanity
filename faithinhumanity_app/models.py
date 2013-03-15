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
    id_str  = models.CharField(unique=True, max_length=255)
    is_good = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return u'Tweet ID: %s [%s]' % (self.id_str, "GOOD" if self.is_good else "BAD" if self.is_good is False else "UNSURE")
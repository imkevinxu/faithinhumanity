from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from coffin.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from faithinhumanity_app.models import *
from faithinhumanity_app.model_forms import *
from faithinhumanity_app.forms import *

import datetime
from math import log,pow,exp

def reference_seconds(date, reference_date):
    """Returns the number of seconds from the reference date.  Credit goes to http://amix.dk/blog/post/19588"""
    td = date - reference_date
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def score(tweet, reference_date):
    return 1/(1+exp(-(reference_seconds(tweet.created_at, reference_date)-43200)/10000))

def index(request):
    current_time = timezone.now()
    one_day_ago = current_time + datetime.timedelta(days=-1)

    tweets = Tweet.objects.filter(created_at__range=[one_day_ago, current_time]).order_by('-created_at')
    good_tweets = tweets.filter(is_good=True)
    bad_tweets = tweets.filter(is_good=False)
    good_tweets_without_retweets = good_tweets.filter(is_retweet=False)
    bad_tweets_without_retweets = bad_tweets.filter(is_retweet=False)

    good_score_acc = sum(map(score, good_tweets, [one_day_ago]*len(good_tweets)))
    bad_score_acc = sum(map(score, bad_tweets, [one_day_ago]*len(bad_tweets)))

    good_score = int((good_score_acc/(good_score_acc + bad_score_acc)) * 100)
    bad_score = 100 - good_score

    return render(request, "index.html", locals())

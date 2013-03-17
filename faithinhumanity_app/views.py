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

from faithinhumanity_app.models import *
from faithinhumanity_app.model_forms import *
from faithinhumanity_app.forms import *

import datetime

def index(request):
    tweets = Tweet.objects.filter(created_at__range=[datetime.datetime.now()  + datetime.timedelta(days=-1), datetime.datetime.now()])
    good_tweets = tweets.filter(is_good=True)
    bad_tweets = tweets.filter(is_good=False)

    good_score = round((float(len(good_tweets))/len(tweets)) * 100)
    bad_score = 100 - good_score

    return render(request, "index.html", locals())

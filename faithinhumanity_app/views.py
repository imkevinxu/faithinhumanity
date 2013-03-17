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

def index(request):
    current_time = timezone.now()
    one_day_ago = current_time + datetime.timedelta(days=-1)

    tweets = Tweet.objects.filter(created_at__range=[one_day_ago, current_time]).order_by('-created_at')
    good_tweets = tweets.filter(is_good=True)
    bad_tweets  = tweets.filter(is_good=False)

    good_score = int((float(len(good_tweets)) / len(tweets) if len(tweets) > 0 else 1) * 100)
    bad_score = 100 - good_score

    return render(request, "index.html", locals())

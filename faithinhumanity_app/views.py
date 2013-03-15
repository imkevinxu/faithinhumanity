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

#@login_required
def index(request):
    # tweet = Tweet(tweet_id_string="231531", original_tweet_creation=datetime.datetime.now(), is_good=True)
    # tweet.save()
    return render(request, "index.html", locals())

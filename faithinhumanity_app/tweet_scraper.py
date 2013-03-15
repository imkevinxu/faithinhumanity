# -*- coding: utf-8 -*-

import sys
import tweepy
import webbrowser
import datetime

from faithinhumanity_app.models import Tweet

goodStatuses = []
badStatuses = []

# Query terms

Q = ['faith in humanity', 'faithinhumanity']

positiveWords = ['restored', 'restoring', 'restore', 'returns']
negativeWords = ['lose', 'loseing', 'lost', 'losing', 'no']

# Get these values from your application settings.

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Get these values from the "My Access Token" link located in the
# margin of your application details, or perform the full OAuth
# dance.

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Note: Had you wanted to perform the full OAuth dance instead of using
# an access key and access secret, you could have uses the following 
# four lines of code instead of the previous line that manually set the
# access token via auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET).
# 
# auth_url = auth.get_authorization_url(signin_with_twitter=True)
# webbrowser.open(auth_url)
# verifier = raw_input('PIN: ').strip()
# auth.get_access_token(verifier)

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        # We'll simply print some values in a tab-delimited format
        # suitable for capturing to a flat file but you could opt 
        # store them elsewhere, retweet select statuses, etc.

        try:
            if any(word in status.text for word in positiveWords):
                tweet = Tweet()
                tweet.tweet_id_string = status.id_str
                tweet.original_tweet_creation = datetime.datetime.now()
                tweet.is_good = True
                tweet.save()
                print "postive"
            elif any(word in status.text for word in negativeWords):
                tweet = Tweet()
                tweet.tweet_id_string = status.id_str
                tweet.original_tweet_creation = datetime.datetime.now()
                tweet.is_good = False
                print "negative"
                
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# Create a streaming API and set a timeout value of 60 seconds.

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

# Optionally filter the statuses you want to track by providing a list
# of users to "follow".

streaming_api.filter(follow=None, track=Q, async=False)

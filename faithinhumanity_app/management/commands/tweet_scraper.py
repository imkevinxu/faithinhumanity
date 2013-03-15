import os
import sys
import tweepy
import datetime

from django.core.management.base import BaseCommand, CommandError
from faithinhumanity_app.models import Tweet

CONSUMER_KEY        = os.environ.get('TWITTER_FAITH_CONSUMER_KEY')
CONSUMER_SECRET     = os.environ.get('TWITTER_FAITH_CONSUMER_SECRET')
ACCESS_TOKEN        = os.environ.get('TWITTER_FAITH_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_FAITH_ACCESS_TOKEN_SECRET')

# Query terms
# TODO: find typos in query
# TODO: find more positives and negatives
query    = ['faith in humanity', 'faithinhumanity']
positives = ['restore', 'restores', 'restored', 'restoring', 'gain', 'gains', 'gained', 'gaining', \
             'return', 'returns', 'returned', 'returning', 'alive']
negatives = ['lose', 'loses', 'lost', 'losing', 'loseing', 'no']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self, api=None):
        self.api = api or tweepy.API()
        print 'Tweet Scraper Initializing'

    def on_status(self, status):
        try:
            tweet = Tweet() #TODO: Incorporate more fields
            tweet.id_str = status.id_str
            if any(word in status.text.lower() for word in positives):
                tweet.is_good = True
                tweet.save()
                print '[Saved] %s' % tweet
            elif any(word in status.text.lower() for word in negatives):
                tweet.is_good = False
                tweet.save()
                print '[Saved] %s' % tweet
            else:
                #TODO: Do something with unsure tweets
                print '[Not Saved] %s' % tweet

        except Exception, e:
            print >> sys.stderr, 'Encountered Exception: ', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code: ', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


class Command(BaseCommand):
    def handle(self, *args, **options):
        streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)
        streaming_api.filter(track=query)
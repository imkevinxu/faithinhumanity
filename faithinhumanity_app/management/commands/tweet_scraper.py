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
query     = ['faith in humanity', 'faithinhumanity']
positives = ['restore', 'restores', 'restored', 'restoring', 'gain', 'gains', 'gained', 'gaining', \
             'return', 'returns', 'returned', 'returning', 'reaffirm', 'reaffirms', 'reaffirmed', 'reaffirming', \
             'give', 'gives', 'gave', 'giving', 'renew', 'renews', 'renewed', 'alive', 'back', 'rises', 'rising']
negatives = ['lose', 'loses', 'lost', 'losing', 'loseing', 'destroy', 'destroys', 'destroyed', 'destroying', \
             'decrease', 'decreases', 'decreased', 'decreasing', 'dim', 'dimmer', 'dims', 'dimmed', 'dimming', \
             'loss', 'no', 'little', 'goodbye', 'negative', 'dead', 'plummet', 'plummeted', 'plummeting', \
             'lower', 'lowers', 'lowering', 'lowered', 'no more', 'loose', 'loosing', 'gone', 'lessens', \
             'lack', 'low', 'crush', 'crushes', 'crushing', 'crushed', 'dwindling', 'dwindled']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self, api=None):
        self.api = api or tweepy.API()
        print 'Tweet Scraper Initializing'

    def tweet_from_status(self, status):
        tweet = Tweet()
        tweet.id_str = status.id_str
        tweet.text = status.text
        tweet.username = status.user.name
        tweet.screenname = status.user.screen_name
        tweet.profile_image_url = status.user.profile_image_url.replace('normal', 'bigger')
        tweet.is_retweet = True if hasattr(status, 'retweeted_status') else False
        return tweet

    def on_status(self, status):
        if any(q in status.text.lower() for q in query):
            try:
                tweet = self.tweet_from_status(status)

                if any(word in status.text.lower() for word in positives):
                    tweet.is_good = True
                    tweet.save()
                    print '[Saved] %s' % tweet
                elif any(word in status.text.lower() for word in negatives):
                    tweet.is_good = False
                    tweet.save()
                    print '[Saved] %s' % tweet
                else:
                    print '[NOT SAVED] %s' % tweet

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

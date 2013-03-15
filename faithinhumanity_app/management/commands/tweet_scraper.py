import sys
import tweepy
import webbrowser
import datetime
import os

from django.core.management.base import BaseCommand, CommandError
from faithinhumanity_app.models import Tweet

CONSUMER_KEY = os.environ.get('TWITTER_FAITH_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_FAITH_CONSUMER_SECRET')

ACCESS_TOKEN = os.environ.get('TWITTER_FAITH_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_FAITH_ACCESS_TOKEN_SECRET')

# Query terms

Q = ['faith in humanity', 'faithinhumanity']

positiveWords = ['restored', 'restoring', 'restore', 'returns']
negativeWords = ['lose', 'loseing', 'lost', 'losing', 'no']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

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
                tweet.save()
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


class Command(BaseCommand):
    def handle(self, *args, **options):
        streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)
        streaming_api.filter(follow=None, track=Q, async=False)





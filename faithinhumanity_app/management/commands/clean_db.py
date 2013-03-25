from django.core.management.base import BaseCommand, CommandError
from faithinhumanity_app.models import Tweet

import sys

class Command(BaseCommand):
    def handle(self, *args, **options):
        print >> sys.stdout, '\n[Clean DB] Initializing...'
        try:
            total_tweets = Tweet.objects.all()
            if len(total_tweets) >= 9000:
                objects_to_keep = Tweet.objects.all()[10:]
                Tweet.objects.exclude(pk__in=objects_to_keep).delete()
                print >> sys.stdout, 'DB Successfully Cleaned'
                print >> sys.stdout, 'From %s rows -> %s rows' % (len(total_tweets), len(Tweet.objects.all()))
            else:
                print >> sys.stdout, 'DB Not Cleaned'
                print >> sys.stdout, 'Currently has only %s rows' % len(total_tweets)

        except Exception, e:
            print >> sys.stderr, 'Encountered Exception: ', e
            pass
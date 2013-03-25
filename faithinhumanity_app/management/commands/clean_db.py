from django.core.management.base import BaseCommand, CommandError
from faithinhumanity_app.models import Tweet

class Command(BaseCommand):
    def handle(self, *args, **options):
        total_tweets = Tweet.objects.all()
        if len(total_tweets) >= 9000:
            objects_to_keep = Tweet.objects.all()[1000:]
            Tweet.objects.exclude(pk__in=objects_to_keep).delete()
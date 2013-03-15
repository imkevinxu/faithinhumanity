from django.core.management.base import BaseCommand, CommandError
from faithinhumanity_app.models import Tweet

class Command(BaseCommand):
    def handle(self, *args, **options):
        # your code here
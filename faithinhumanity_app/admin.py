from faithinhumanity_app.models import *
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet_id_string', 'is_good', 'original_tweet_creation', 'created_at')
    list_filter = ('is_good',)
    ordering = ['-original_tweet_creation']
    search_fields = ['tweet_id_string', 'is_good']

admin.site.register(Tweet, TweetAdmin)
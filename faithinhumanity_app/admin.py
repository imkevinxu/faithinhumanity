from faithinhumanity_app.models import *
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    list_display = ('username', 'screenname', 'text', 'is_good', 'is_retweet', 'created_at')
    list_filter = ('is_good', 'is_retweet')
    ordering = ['-created_at', 'id_str']
    search_fields = ['username', 'screenname', 'text']

admin.site.register(Tweet, TweetAdmin)
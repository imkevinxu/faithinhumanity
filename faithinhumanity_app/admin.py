from faithinhumanity_app.models import *
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    list_display = ('username', 'screenname', 'text', 'is_good', 'created_at')
    list_filter = ('is_good',)
    ordering = ['-created_at', 'id_str']
    search_fields = ['username', 'screenname', 'text']

admin.site.register(Tweet, TweetAdmin)
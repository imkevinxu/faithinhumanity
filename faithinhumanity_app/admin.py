from faithinhumanity_app.models import *
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    list_display = ('id_str', 'is_good', 'created_at')
    list_filter = ('is_good',)
    ordering = ['-created_at']
    search_fields = ['id_str', 'is_good']

admin.site.register(Tweet, TweetAdmin)
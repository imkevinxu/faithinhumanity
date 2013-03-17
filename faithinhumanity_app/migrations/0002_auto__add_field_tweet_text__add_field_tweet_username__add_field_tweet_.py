# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tweet.text'
        db.add_column('faithinhumanity_app_tweet', 'text',
                      self.gf('django.db.models.fields.CharField')(default='text', max_length=255),
                      keep_default=False)

        # Adding field 'Tweet.username'
        db.add_column('faithinhumanity_app_tweet', 'username',
                      self.gf('django.db.models.fields.CharField')(default='text', max_length=255),
                      keep_default=False)

        # Adding field 'Tweet.screenname'
        db.add_column('faithinhumanity_app_tweet', 'screenname',
                      self.gf('django.db.models.fields.CharField')(default='text', max_length=255),
                      keep_default=False)

        # Adding field 'Tweet.profile_image_url'
        db.add_column('faithinhumanity_app_tweet', 'profile_image_url',
                      self.gf('django.db.models.fields.URLField')(default='text', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tweet.text'
        db.delete_column('faithinhumanity_app_tweet', 'text')

        # Deleting field 'Tweet.username'
        db.delete_column('faithinhumanity_app_tweet', 'username')

        # Deleting field 'Tweet.screenname'
        db.delete_column('faithinhumanity_app_tweet', 'screenname')

        # Deleting field 'Tweet.profile_image_url'
        db.delete_column('faithinhumanity_app_tweet', 'profile_image_url')


    models = {
        'faithinhumanity_app.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'is_good': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'screenname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['faithinhumanity_app']
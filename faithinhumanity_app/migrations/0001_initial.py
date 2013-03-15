# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table('faithinhumanity_app_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('tweet_id_string', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('original_tweet_creation', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_good', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('faithinhumanity_app', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table('faithinhumanity_app_tweet')


    models = {
        'faithinhumanity_app.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_good': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'original_tweet_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_id_string': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['faithinhumanity_app']
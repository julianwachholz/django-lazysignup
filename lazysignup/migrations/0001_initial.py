# flake8: noqa
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from .helper import *


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LazyUser'
        db.create_table('lazysignup_lazyuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[USER_MODEL], unique=True)),
        ))
        db.send_create_signal('lazysignup', ['LazyUser'])


    def backwards(self, orm):
        
        # Deleting model 'LazyUser'
        db.delete_table('lazysignup_lazyuser')


    models = {
        'lazysignup.lazyuser': {
            'Meta': {'object_name': 'LazyUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': 'orm["'+USER_MODEL+'"]', 'unique': 'True'})
        },
        USER_MODEL: USER_MODEL_DICT,
    }

    complete_apps = ['lazysignup']

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LazyUser.user'
        db.alter_column('lazysignup_lazyuser', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm[USER_MODEL], unique=True))
        # Adding index on 'LazyUser', fields ['created']
        db.create_index('lazysignup_lazyuser', ['created'])


    def backwards(self, orm):
        # Removing index on 'LazyUser', fields ['created']
        db.delete_index('lazysignup_lazyuser', ['created'])


        # Changing field 'LazyUser.user'
        db.alter_column('lazysignup_lazyuser', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[USER_MODEL], unique=True))

    models = {
        'lazysignup.lazyuser': {
            'Meta': {'object_name': 'LazyUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.User']", 'unique': 'True'})
        },
    }

    complete_apps = ['lazysignup']

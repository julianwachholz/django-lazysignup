# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LazyUser.created'
        db.add_column('lazysignup_lazyuser', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LazyUser.created'
        db.delete_column('lazysignup_lazyuser', 'created')


    models = {
        'lazysignup.lazyuser': {
            'Meta': {'object_name': 'LazyUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
    }

    complete_apps = ['lazysignup']

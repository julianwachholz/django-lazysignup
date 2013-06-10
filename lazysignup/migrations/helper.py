# -*- coding: utf-8 -*-

from django.conf import settings


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

# This dict should be used in the ``models`` field of a migration.
USER_MODEL_DICT = {
    'Meta': {'object_name': User.__name__},
    'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
}

# Dummy migration because South will try to migrate all modules.

from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {}
    complete_apps = []

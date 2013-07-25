# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Introduction'
        db.create_table(u'system_introduction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Language'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'system', ['Introduction'])


    def backwards(self, orm):
        # Deleting model 'Introduction'
        db.delete_table(u'system_introduction')


    models = {
        u'system.introduction': {
            'Meta': {'object_name': 'Introduction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Language']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'system.language': {
            'Meta': {'object_name': 'Language'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['system']
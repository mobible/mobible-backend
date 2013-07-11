# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('system', '0001_initial'),
    )

    def forwards(self, orm):
        # Adding field 'Journey.language'
        db.add_column(u'dbs_journey', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['system.Language']),
                      keep_default=False)


        # Changing field 'Verse.index'
        db.alter_column(u'dbs_verse', 'index', self.gf('django.db.models.fields.PositiveIntegerField')())

    def backwards(self, orm):
        # Deleting field 'Journey.language'
        db.delete_column(u'dbs_journey', 'language_id')


        # Changing field 'Verse.index'
        db.alter_column(u'dbs_verse', 'index', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'dbs.journey': {
            'Meta': {'object_name': 'Journey'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Language']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dbs.verse': {
            'Meta': {'object_name': 'Verse'},
            'context': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'journey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dbs.Journey']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'verse': ('django.db.models.fields.TextField', [], {})
        },
        u'system.language': {
            'Meta': {'object_name': 'Language'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['dbs']
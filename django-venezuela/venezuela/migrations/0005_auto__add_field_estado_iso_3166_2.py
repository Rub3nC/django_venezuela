# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Estado.iso_3166_2'
        db.add_column(u'venezuela_estado', 'iso_3166_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Estado.iso_3166_2'
        db.delete_column(u'venezuela_estado', 'iso_3166_2')


    models = {
        u'venezuela.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venezuela.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'venezuela.estado': {
            'Meta': {'object_name': 'Estado'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_3166_2': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'venezuela.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venezuela.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'venezuela.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venezuela.Municipio']"}),
            'parroquia': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['venezuela']